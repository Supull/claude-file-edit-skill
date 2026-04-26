---
name: file-edit
description: "Use this skill whenever the user asks you to make a code change, edit a file, replace a component, add an import, delete a block, or modify anything in their codebase. Instead of showing the updated file or reprinting code, always output a ready-to-paste python3 heredoc terminal command that the user can copy and run directly in their terminal. The heredoc uses with open() to read the file, replaces the exact old string with the new string, prints success or NOT FOUND, then writes back. Never reprint the whole file. Never show a diff. Just output the pasteable heredoc command."
license: MIT
---

# File Edit Skill

## What this skill does

When a user asks for a code change, output a **ready-to-paste terminal command** using a Python heredoc. The user copies it, pastes it into their terminal, and it edits the file directly. No file reprinting, no diffs, no copy-pasting individual code blocks.

## Output format — always use this

```bash
python3 << 'EOF'
with open('PATH/TO/FILE', 'r') as f:
    content = f.read()
old = '''EXACT_OLD_STRING'''
new = '''NEW_STRING'''
if old in content:
    content = content.replace(old, new)
    print("replaced successfully")
else:
    print("NOT FOUND")
with open('PATH/TO/FILE', 'w') as f:
    f.write(content)
EOF
```

## Why this matters

On the free tier every message counts. Reprinting a 400-line file to change 10 lines wastes the majority of the response on unchanged code. A heredoc only contains the lines that actually changed — same result, fraction of the tokens.

## If the user shares their file structure

The user may paste output from `find . -type f | grep -v node_modules | grep -v .git` before asking for a change. Use it to get the exact file path right in the `with open()`. If they don't share it, ask for the path before generating the heredoc.

## Rules

1. `old` must be the **exact** string from the file — preserve all whitespace, indentation, and newlines
2. Always include the `if old in content / else NOT FOUND` guard
3. Use triple quotes `'''` for old/new strings so multiline code works
4. Never reprint the whole file
5. Never show a diff
6. Never say "here's the updated file" — just give the heredoc
7. The user will paste and run this in their own terminal

## Patterns

### Replace (default)
Use for any substitution — swapping a component, changing a value, updating a function.

```bash
python3 << 'EOF'
with open('src/pages/Dashboard.tsx', 'r') as f:
    content = f.read()
old = '''                      <button
                        onClick={() => handleCompleteSwap(match, matchIds[i])}
                        className="mt-3 w-full text-sm bg-green-500 hover:bg-green-600 text-white font-semibold py-2.5 rounded-xl transition-colors"
                      >
                        ✅ I completed my swap in MyUTK
                      </button>'''
new = '''                      <CompletedButton
                        match={match}
                        matchId={matchIds[i]}
                        userId={user!.id}
                        onComplete={handleCompleteSwap}
                      />'''
if old in content:
    content = content.replace(old, new)
    print("replaced successfully")
else:
    print("NOT FOUND")
with open('src/pages/Dashboard.tsx', 'w') as f:
    f.write(content)
EOF
```

### Insert after anchor
Use when adding an import, a line, or a block after a specific line.

```bash
python3 << 'EOF'
with open('src/pages/Dashboard.tsx', 'r') as f:
    content = f.read()
anchor = '''import MatchChat from '../components/MatchChat' '''
insertion = '''
import CompletedButton from '../components/CompletedButton' '''
if anchor in content:
    content = content.replace(anchor, anchor + insertion, 1)
    print("inserted successfully")
else:
    print("NOT FOUND")
with open('src/pages/Dashboard.tsx', 'w') as f:
    f.write(content)
EOF
```

### Delete a block
Use when removing dead code, a component, or a section.

```bash
python3 << 'EOF'
with open('src/pages/Dashboard.tsx', 'r') as f:
    content = f.read()
block = '''                      <button
                        onClick={() => handleCompleteSwap(match, matchIds[i])}
                      >
                        ✅ I completed my swap
                      </button>'''
if block in content:
    content = content.replace(block, '')
    print("deleted successfully")
else:
    print("NOT FOUND")
with open('src/pages/Dashboard.tsx', 'w') as f:
    f.write(content)
EOF
```

### Multiple changes to same file
Chain multiple replacements in one heredoc.

```bash
python3 << 'EOF'
with open('src/pages/Dashboard.tsx', 'r') as f:
    content = f.read()

changes = [
    ('''old string 1''', '''new string 1'''),
    ('''old string 2''', '''new string 2'''),
]

for old, new in changes:
    if old in content:
        content = content.replace(old, new)
        print(f"replaced: {old[:40].strip()}...")
    else:
        print(f"NOT FOUND: {old[:40].strip()}...")

with open('src/pages/Dashboard.tsx', 'w') as f:
    f.write(content)
EOF
```

### Debug: NOT FOUND
If the user says the command printed NOT FOUND, output this to help diagnose:

```bash
python3 << 'EOF'
with open('PATH/TO/FILE', 'r') as f:
    content = f.read()
target = '''WHAT_YOU_SEARCHED_FOR'''
if target in content:
    idx = content.index(target)
    print("FOUND. Context:")
    print(repr(content[max(0, idx-100):idx+len(target)+100]))
else:
    print("NOT FOUND. First 600 chars:")
    print(repr(content[:600]))
EOF
```
# claude-file-edit-skill

A Claude skill for making precise, surgical file edits using the bash tool on **claude.ai web** (computer use environment).

## Why use this?

Without this skill, Claude's default when you say "add an import to this file" is to read the whole file, reprint the entire thing with the change, and write it back. On a 500-line file that's wasteful. On a 2000-line file it's genuinely painful — slow, burns through your message limits, and you have to scroll past a wall of unchanged code.

With this skill, Claude does a 10-line heredoc instead. Same result, way less output.

**Concrete benefits:**
- **Faster responses** — no waiting for Claude to reprint your entire codebase
- **Uses fewer messages** — big files don't blow up your context/usage limits
- **Safer** — the `NOT FOUND` guard means Claude never silently fails or corrupts a file
- **Consistent** — Claude always reaches for the same reliable pattern instead of improvising each time
- **Debuggable** — when a match fails, `dry_run.py` shows exact whitespace/newlines so Claude can fix it immediately instead of guessing

## Structure

```
claude-file-edit-skill/
├── SKILL.md                  ← skill instructions + routing table
├── scripts/
│   ├── replace.py            ← replace a string or block
│   ├── insert_after.py       ← insert after an anchor line
│   ├── insert_before.py      ← insert before an anchor line
│   ├── delete_block.py       ← remove a block entirely
│   ├── replace_nth.py        ← replace only the Nth occurrence
│   ├── multi_file.py         ← same change across multiple files
│   ├── dry_run.py            ← verify/inspect before editing
│   └── append.py             ← append to end of file
├── README.md
└── LICENSE
```

Claude reads `SKILL.md` to decide which script to use, then loads only that script's template — keeping token usage minimal.

## Example

```bash
python3 << 'EOF'
with open('src/pages/Dashboard.tsx', 'r') as f:
    content = f.read()

old = "import MatchChat from '../components/MatchChat'"
new = "import MatchChat from '../components/MatchChat'\nimport CompletedButton from '../components/CompletedButton'"

if old in content:
    content = content.replace(old, new)
    print("replaced successfully")
else:
    print("NOT FOUND — check spacing/indentation")

with open('src/pages/Dashboard.tsx', 'w') as f:
    f.write(content)
EOF
```

## Environment

**Only works on claude.ai web/desktop with code execution enabled.**

| Works | Doesn't work |
|-------|-------------|
| claude.ai web (code execution on) | Claude Code — has native file tools, doesn't need this |
| claude.ai desktop (computer use) | API without computer use |

## Installation

### claude.ai (web)

1. Download this repo as a ZIP (`Code → Download ZIP` on GitHub)
2. **Check the ZIP structure** — the skill folder must be at the root, not double-nested. When you unzip it should look like `claude-file-edit-skill/SKILL.md`, not `claude-file-edit-skill/claude-file-edit-skill/SKILL.md`. If it's double-nested, just move the inner folder out before rezipping.
3. Go to **claude.ai → profile icon → Settings → Features → Skills**
4. Click **Upload** and select the ZIP
5. Make sure **Code Execution** is enabled under **Settings → Capabilities**

Claude will automatically use the skill whenever you ask it to edit files.



## License

MIT
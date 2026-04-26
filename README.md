# claude-file-edit-skill

A Claude skill that makes Claude output ready-to-paste terminal commands for file edits, instead of reprinting your whole file.

## Why use this?

Without this skill, when you ask Claude to make a code change on claude.ai, it typically responds by reprinting your entire file with the change buried somewhere inside. You have to scroll through hundreds of lines of unchanged code, manually copy the relevant parts, and paste them back into your editor.

With this skill, Claude responds with a single copy-paste terminal command:

```bash
python3 << 'EOF'
with open('src/pages/Dashboard.tsx', 'r') as f:
    content = f.read()
old = '''                      <button
                        onClick={() => handleCompleteSwap(match, matchIds[i])}
                        className="mt-3 w-full text-sm bg-green-500 hover:bg-green-600 text-white font-semibold py-2.5 rounded-xl transition-colors"
                      >
                        ✅ I completed my swap
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

Paste it in your terminal, hit enter, done. The file is edited. No scrolling, no manual copy-pasting, no risk of accidentally missing a line.

## Why heredocs save your token budget

On the free tier every message counts. When Claude reprints a 400-line file just to change 10 lines, it burns through your daily limit fast. A heredoc only contains the lines that actually changed — same result, fraction of the tokens. The bigger your files, the more you save.

## Pro tip: show Claude your file structure first

Before asking for a code change, paste your project structure so Claude knows the exact file paths:

```bash
find . -type f | grep -v node_modules | grep -v .git
```

Or just paste the relevant part manually. Claude needs the correct path to fill in the `with open()` — if the path is wrong the command will error out.

## How it works

The heredoc runs Python inline in your terminal. It opens the file, finds the exact old string, replaces it with the new one, and writes it back. The `NOT FOUND` guard means it never silently fails — if the string doesn't match exactly, it tells you.

## Patterns included

- Replace a string or block
- Insert after an anchor line (e.g. adding an import)
- Delete a block
- Multiple changes to the same file in one command
- Debug mode when NOT FOUND

## Environment

Works anywhere you have a terminal — the skill just changes what Claude outputs on claude.ai web. No code execution needed inside Claude.

| Works | Doesn't apply |
|-------|--------------|
| claude.ai web (free or Pro) | Claude Code — already has native file tools |
| claude.ai desktop | |
| Any OS with Python 3 in terminal | |

## Installation

1. Download this repo as a ZIP (`Code → Download ZIP` on GitHub)
2. Go to **claude.ai → profile icon → Settings → Features → Skills**
3. Click **Upload** and select the ZIP
4. Check the ZIP isn't double-nested before uploading — it should be `claude-file-edit-skill/SKILL.md` not `claude-file-edit-skill/claude-file-edit-skill/SKILL.md`

Claude will now respond to code change requests with a pasteable heredoc instead of reprinting your file.

## License

MIT

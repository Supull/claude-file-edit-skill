---
name: file-edit
description: "Use this skill for ANY file editing task in the bash tool environment on claude.ai web. Triggers: inserting a line, replacing a block of code, adding an import, deleting a section, renaming across a file, or any find-and-replace on disk. Also use for multi-file edits, dry-run verification before editing, and safe atomic rewrites. Use this skill instead of rewriting whole files — it saves tokens and is safer. Trigger on phrases like 'add import', 'replace this line', 'remove that block', 'edit the file', 'update the function', 'fix that string'. NOT for Claude Code CLI (has native tools)."
license: MIT
---

# File Editing via Python Heredoc

## Overview

Precise file edits via inline Python heredocs. Safer and cheaper than rewriting whole files — only the changed lines are ever in context.

**Environment:** claude.ai web with code execution (bash tool)

## Token-saving principle

Never read a whole file into the response just to change 2 lines. The heredoc runs in bash — the file content never enters Claude's context window. This keeps edits fast and cheap regardless of file size.

## Quick Reference

| Task | Script |
|------|--------|
| Replace a string/block | `scripts/replace.py` |
| Insert after a line | `scripts/insert_after.py` |
| Insert before a line | `scripts/insert_before.py` |
| Delete a block | `scripts/delete_block.py` |
| Replace nth occurrence | `scripts/replace_nth.py` |
| Edit multiple files | `scripts/multi_file.py` |
| Verify before editing | `scripts/dry_run.py` |
| Append to end of file | `scripts/append.py` |

Read the relevant script when you need the heredoc template, then inline it into a bash call. Don't load scripts you don't need.

## Core rules

1. Always include the `if old in content / else NOT FOUND` guard
2. Exact match only — whitespace, indentation, and newlines matter
3. When `NOT FOUND`, use `dry_run.py` to inspect before retrying
4. Backup before risky or multi-step edits: `cp file.ext file.ext.bak`
5. After editing, verify: `grep -n "new string" path/to/file`

## When to use which script

- **Single targeted change** → `replace.py`
- **Adding a line/import near an anchor** → `insert_after.py` or `insert_before.py`
- **Removing dead code** → `delete_block.py`
- **Same change across many files** → `multi_file.py`
- **Unsure of exact spacing/content** → `dry_run.py` first, then edit
- **Adding content at end** → `append.py`
- **Duplicate strings in file** → `replace_nth.py`

## Windows line endings

If edits fail on Windows-originated files, add after reading:
```python
content = content.replace('\r\n', '\n')
```
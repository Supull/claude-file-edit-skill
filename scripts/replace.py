# Usage: inline this as a python3 heredoc in bash
# Replace FILE_PATH, OLD_STRING, NEW_STRING with actual values

python3 << 'EOF'
with open('FILE_PATH', 'r') as f:
    content = f.read()

old = """OLD_STRING"""

new = """NEW_STRING"""

if old in content:
    content = content.replace(old, new)
    print("replaced successfully")
else:
    print("NOT FOUND — check spacing/indentation (use dry_run.py to inspect)")

with open('FILE_PATH', 'w') as f:
    f.write(content)
EOF
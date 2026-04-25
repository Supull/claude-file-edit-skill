# Usage: inline this as a python3 heredoc in bash
# Inserts INSERTION immediately after ANCHOR_LINE (first occurrence)

python3 << 'EOF'
with open('FILE_PATH', 'r') as f:
    content = f.read()

anchor = """ANCHOR_LINE"""
insertion = "\nINSERTION"

if anchor in content:
    content = content.replace(anchor, anchor + insertion, 1)
    print("inserted successfully")
else:
    print("NOT FOUND — anchor line missing (use dry_run.py to inspect)")

with open('FILE_PATH', 'w') as f:
    f.write(content)
EOF
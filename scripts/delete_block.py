# Usage: inline this as a python3 heredoc in bash
# Deletes BLOCK_TO_DELETE entirely from the file

python3 << 'EOF'
with open('FILE_PATH', 'r') as f:
    content = f.read()

block = """BLOCK_TO_DELETE"""

if block in content:
    content = content.replace(block, '')
    print("block deleted successfully")
else:
    print("NOT FOUND — check exact content (use dry_run.py to inspect)")

with open('FILE_PATH', 'w') as f:
    f.write(content)
EOF
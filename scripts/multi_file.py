# Usage: inline this as a python3 heredoc in bash
# Applies the same replacement across multiple files

python3 << 'EOF'
import os

files = [
    'path/to/file1.ts',
    'path/to/file2.ts',
    'path/to/file3.ts',
]

old = """OLD_STRING"""
new = """NEW_STRING"""

for filepath in files:
    if not os.path.exists(filepath):
        print(f"SKIP (file not found): {filepath}")
        continue
    with open(filepath, 'r') as f:
        content = f.read()
    if old in content:
        content = content.replace(old, new)
        with open(filepath, 'w') as f:
            f.write(content)
        print(f"OK: {filepath}")
    else:
        print(f"NOT FOUND: {filepath}")
EOF
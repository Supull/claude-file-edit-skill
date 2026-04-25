# Usage: inline this as a python3 heredoc in bash
# Run this BEFORE editing when NOT FOUND or unsure of exact spacing.
# Shows surrounding context around the target string.

python3 << 'EOF'
with open('FILE_PATH', 'r') as f:
    content = f.read()

target = """TARGET_STRING"""

if target in content:
    idx = content.index(target)
    start = max(0, idx - 100)
    end = idx + len(target) + 100
    print("FOUND. Context around match:")
    print(repr(content[start:end]))
else:
    print("NOT FOUND.")
    print("\nFirst 600 chars of file:")
    print(repr(content[:600]))
    print("\nLast 300 chars of file:")
    print(repr(content[-300:]))
    # Also show line count to confirm you have the right file
    print(f"\nTotal lines: {content.count(chr(10))}")
EOF
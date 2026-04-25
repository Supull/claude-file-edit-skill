# Usage: inline this as a python3 heredoc in bash
# Replaces only the Nth occurrence (1-based) of TARGET with REPLACEMENT

python3 << 'EOF'
with open('FILE_PATH', 'r') as f:
    content = f.read()

target = """TARGET"""
replacement = """REPLACEMENT"""
n = 1  # which occurrence to replace (1 = first)

parts = content.split(target)
if len(parts) > n:
    content = target.join(parts[:n]) + replacement + target.join(parts[n:])
    print(f"replaced occurrence #{n} successfully")
else:
    count = len(parts) - 1
    print(f"NOT FOUND — only {count} occurrence(s) exist, wanted #{n}")

with open('FILE_PATH', 'w') as f:
    f.write(content)
EOF
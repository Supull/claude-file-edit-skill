# Usage: inline this as a python3 heredoc in bash
# Appends CONTENT to the end of the file (with a newline separator)

python3 << 'EOF'
with open('FILE_PATH', 'a') as f:
    f.write("\nCONTENT_TO_APPEND")
print("appended successfully")
EOF
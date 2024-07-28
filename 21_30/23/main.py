import subprocess

# Str, Chạy 1 cmd trong terminal và lấy output
## Cmd: strings -4 /etc/issue
print(subprocess.check_output(["strings", "-4", "/etc/issue"]))

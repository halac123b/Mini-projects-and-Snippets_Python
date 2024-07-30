import subprocess

try:
    # Str, Chạy 1 cmd trong terminal và lấy output
    ## Cmd: strings -4 /etc/issue
    print(subprocess.check_output(["strings", "-4", "/etc/issue"]))

# throw khi subprocess exit và return kết quả khác 0
except subprocess.CalledProcessError as e:
    print("CalledProcessError")

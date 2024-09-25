import subprocess
import sys

try:
    # Str, Chạy 1 cmd trong terminal và lấy output
    ## Cmd: strings -4 /etc/issue
    print(subprocess.check_output(["strings", "-4", "/etc/issue"]))

    # Chạy 1 lệnh trong terminal
    ## input: list các item trong cmd, trong lệnh chúng cách nhau bằng dấu cách
    ## return: nếu lệnh chạy ok return 0, else raise exception bên dưới
    ## Đây là hàm blocking, gọi thì chương trình sẽ dừng cho tới khi nó chạy xog
    subprocess.check_call([sys.executable, "-m", "pip", "install", "python-socketio"])

# throw khi subprocess exit và return kết quả khác 0
except subprocess.CalledProcessError as e:
    print("CalledProcessError")

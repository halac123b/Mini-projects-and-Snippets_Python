import os
import signal
import sys

# Access, modify or add new OS environment variables
## Use as a dict
## Value is string type
## Tác dụng khi modify chỉ tồn tại trong khi chương trình chạy lần đó, chạy xong về như cũ
os.environ["some_env_var"] = "value"

# str: Lấy ra path đến folder chứa file từ path đến file đó
print(os.path.dirname("folder/file.txt"))

# Bool, check xem path đó có tồn tại k
print(os.path.exists("path1/path2"))

# int, id của process đang chạy
print(os.getpid())

# Kết thúc 1 process, với tín hiệu SIGQUIT (tạo core dump)
os.kill(os.getpid(), signal.SIGQUIT)

# Chạy 1 lệnh khác bằng cmd để thay thế cho process hiện tại
## arg[1]: tên cmd
## arg[2]: các arg của cmd
os.execv(sys.argv[0], sys.argv)

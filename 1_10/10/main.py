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

# Bool, check xem path đó có link đến 1 file đã có sẵn không
print(os.path.isfile("path to file"))

# int, id của process đang chạy
print(os.getpid())

# int, ID của user hiện tại đang chạy chương trình
## Nếu quyền admin, UID = 0
print(os.geteuid())

# Kết thúc 1 process, với tín hiệu SIGQUIT (tạo core dump)
os.kill(os.getpid(), signal.SIGQUIT)

# Chạy 1 lệnh khác bằng cmd để thay thế cho process hiện tại
## arg[1]: tên cmd
## arg[2]: các arg của cmd
os.execv(sys.argv[0], sys.argv)

# Rename file hoặc folder
os.rename("filepath", "filepath" + '.bak')

# Set quyền cho file
## 384 = 0o600: rw-------: owner wr, người khác k đc làm gì cả
    # Số này là cố định, cần phải thuộc
# Nếu set quyền mà k có quyền đc set, raise PermissionError exception
os.chmod("path/to/file", 384)

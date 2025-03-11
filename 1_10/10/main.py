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

# int, ID của user hiện tại đang chạy chương trình (effective user id)
## Nếu quyền admin, UID = 0
## Đôi khi k phải ID thực tế của user đó, bị ảnh hưởng bởi role hiện có của user
## vd: user ID = 1000, nhưng role root (sudo), khi đó log geteuid = 0
print(os.geteuid())

# Effective group ID, cũng giống UserID nhưng là cho group của user đó
print(os.getegid())

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

# set process group: Tạo 1 group process mới cho process hiện tại
# Biến nó thành 1 process chạy ngầm, k bị ảnh hưởng bởi những thao tác lên process chính (vd: Ctrl+C để stop)
# Lúc này nếu muốn tắt phải tìm pid và tắt bằng cmd của OS (vẫn có thể dùng os.kill())
os.setpgrp()

# Set user vào group có các ID input
## groups: int[]
os.setgroups(groups)
# Set user ID và group ID cho process hiện tại
os.setgid(gid)
os.setuid(uid)
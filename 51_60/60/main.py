import setproctitle

# Đổi tên process
# Affects các tool để check process như ps, htop
# Nhưng k thực sự đổi tên trong /proc/<pid>/status trên Linux
setproctitle.setproctitle("Process name")
import platform

# Check loại implemetation của Python trên máy đó (CPython, PyPy)
print(platform.python_implementation())

# String: tên version Python hiện tại
print(platform.python_version())

# Tuple, các info về version MacOS (chỉ chạy khi trên Mac, các platform khác k có field này gây lỗi)
print(platform.mac_ver())

# String: tên OS (Linux, Windows,..)
print(platform.system())

# Tuple chứa 3 số về version Python 3.10.13 → ('3', '10', '13')
print(platform.python_version_tuple())

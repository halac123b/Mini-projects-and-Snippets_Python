module_name = "numpy"

# Dynamic import 1 module
## name: tên của module
## fromlist: list các field của module muốn import, nếu lấy chính tên module sẽ tương đương "import module"
module = __import__(name=module_name, fromlist=[module_name])

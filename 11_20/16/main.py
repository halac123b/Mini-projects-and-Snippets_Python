import sys

# Dict, list các package đã đc IMPORT vào project hiện tại đang chạy
print(sys.modules)

# List, các arg đc dùng khi gọi cmd chương trình python
## sys.argv[0]: thông thường, code Python chạy bằng lệnh python → "python"
print(sys.argv)

# str, path đến file executable của Python đc cài đặt trong máy
print(sys.executable)

# Thoát khỏi chương trình đang chạy
## sys.exit(1), sys.exit("Exiting the program with a message.") : có thể kèm theo status code hay msg
sys.exit()

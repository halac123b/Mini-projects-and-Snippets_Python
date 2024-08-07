import sys

# Dict, list các package đã đc IMPORT vào project hiện tại đang chạy
print(sys.modules)

# Thoát khỏi chương trình đang chạy
## sys.exit(1), sys.exit("Exiting the program with a message.") : có thể kèm theo status code hay msg
sys.exit()

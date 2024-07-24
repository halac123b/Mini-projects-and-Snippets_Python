import os

# Access, modify or add new OS environment variables
## Use as a dict
## Value is string type
## Tác dụng khi modify chỉ tồn tại trong khi chương trình chạy lần đó, chạy xong về như cũ
os.environ["some_env_var"] = "value"

# str: Lấy ra path đến folder chứa file từ path đến file đó
print(os.path.dirname("folder/file.txt"))

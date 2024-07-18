import os

# Access, modify or add new OS environment variables
## Use as a dict
## Value is string type
## Tác dụng khi modify chỉ tồn tại trong khi chương trình chạy lần đó, chạy xong về như cũ
os.environ["some_env_var"] = "value"

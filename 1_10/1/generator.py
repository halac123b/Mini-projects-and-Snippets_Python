import random
from fortunes import getFortunes
# Package giúp thêm arg khi ta run code python bằng cmd (python code.py)
import argparse

# Tạo 1 obj Parser chứa các chức năng
parser = argparse.ArgumentParser(description="Python script to randomly generate fortunes")

# Thêm arg, mỗi arg gắn với 1 flag (-c, -v), kèm các thuộc tính giải thích cụ thể
parser.add_argument("-c", required=False, help="How many to return", dest="count", type=int)
parser.add_argument("-v", action="version", version="1.0")

# Thêm arg xong thì parse vào
args = parser.parse_args()

fortunes = getFortunes()

# Access các arg thông qua 'dest' của chúng
if args.count:
    for i in range(args.count):
        print(random.choice(fortunes))
else:
    print(random.choice(fortunes))
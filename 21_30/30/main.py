# package chứa các tool để iterate qua các container
import itertools

# Tạo 1 container bộ đếm vô tận, bắt đầu từ 0, step = 1
counter = itertools.count()

# 0 1 2 3 4
for i in range(5):
    print(next(counter))

# Set các arg vị trí bắt đầu và step
counter = itertools.count(start=10, step=2)

import queue

my_queue = queue.Queue(maxsize=5)

# Add item mới vào cuối queue
my_queue.put(5)

# Get item đầu tiên, xóa item đó luôn
print(my_queue.get())

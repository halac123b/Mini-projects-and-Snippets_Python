import threading
import time


def thread_function(name):
    print(f"Thread start {name}")
    time.sleep(2)
    print(f"Thread end {name}")


# Tạo 1 obj Thread, gồm hàm để nó chạy và arg của hàm đó
thread_1 = threading.Thread(target=thread_function, args=(1,))
print("Before thread start")
# Start thread
thread_1.start()
print("Wait for thread")

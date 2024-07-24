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

# Pause main thread lại để chờ thread_1 chạy xog rồi mới chạy tiếp
thread_1.join()

# Nếu chương trình đã chạy hết mà thread vẫn còn chạy, chương trình vẫn k tắt mà giữ thread chạy ngầm, có thể dùng Ctrl+C để force stop

# Có 1 loại khác: daemon thread, thường dùng cho các tác vụ ngầm và sẽ tắt ngay khi chương trình tắt
daemon_thread = threading.Thread(target=thread_function, args=(1,), daemon=True)

# NOTE: chúng ta có thể control đc lúc nào bắt đầu thread nhưng sau đó thứ tự chạy và kết thúc của chúng do OS lo và ta k control đc
## Thứ tự chạy sẽ khác nhau sau mỗi lần chạy chương trình

# NOTE: khi có nhiều thread nên ưu tiên dùng ThreadPoolExecutor: 21_30\21\futures\main.py

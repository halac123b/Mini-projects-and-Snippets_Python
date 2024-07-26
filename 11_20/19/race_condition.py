import threading
import time


class FakeDatabase:
    def __init__(self):
        self.value = 0
        # Lock, phương tiện giúp quản lí quyền truy cập vào 1 resource giữa các thread
        self._lock = threading.Lock()

    def locked_update(self, name):
        print(f"Thread {name}: starting update")
        # Cấp lock cho thread trong with(), chạy xog tự nhả lock ra
        ## Chỉ có thread giữ lock mới đc modify các biến trong hàm, nếu k thread đó sẽ phải chờ
        with self._lock:
            print(f"Thread {name} has lock")
            local_copy = self.value
            local_copy += 1
            time.sleep(0.1)
            self.value = local_copy
            print(f"Thread {name} release lock")


# NOTE: có 1 lỗi cần phải tránh là Deadlock: khi có 1 chuỗi nối với nhau đều đang chờ lock đc release từ thread khác, khiến hệ thống bị kẹt

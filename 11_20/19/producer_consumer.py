import queue
import threading
import random
import concurrent.futures
import time

SENTINEL = object()


class PipelineOld:
    """Class to allow a single element pipeline between producer and consumer."""

    # NOTE: nhưng cách hiện thực này rất hạn chế khi chỉ 1 msg đc gửi và nhận, cách tối ưu hơn là dùng Queue
    def __init__(self):
        self.message = 0
        self.producer_lock = threading.Lock()
        self.consumer_lock = threading.Lock()
        # Yêu cầu nắm giữ lock
        self.consumer_lock.acquire()

    def get_message(self, name):
        """Consumer"""
        print(f"{name}: about to acquire getlock")
        self.consumer_lock.acquire()
        print(f"{name}:have getlock")
        message = self.message
        print(f"{name}: about to release setlock")
        # Trả lại producer_lock cho chương trình, cho phép nhận msg tiếp theo
        ## Điều này đảm bảo chỉ có 1 msg đc gửi đi tại 1 thời điểm
        ## NOTE: nhưng ngay lúc này có 1 nguy cơ tiềm ẩn, khi producer đc thả ra, nó có thể cập nhật lại msg theo giá trị mới trc khi consumer lưu msg cũ
        self.producer_lock.release()
        print(f"{name}: setlock released")
        return message

    def set_message(self, message, name):
        """Producer"""
        print(f"{name}:about to acquire setlock")
        self.producer_lock.acquire()
        print(f"{name}:have setlock")
        self.message = message
        print(f"{name}:about to release getlock")
        self.consumer_lock.release()
        print(f"{name}:getlock released")


class Pipeline(queue.Queue):
    """Message queue"""

    # Các code liên quan đến lock của thread khi dùng Queue đều k cần
    ## Vì khi dev ngta biết Queue sẽ đc áp dụng rất nhiều trong thread
    ## Nên Queue là thread-safe
    def __init__(self):
        super().__init__(maxsize=10)

    def get_message(self, name):
        print("%s:about to get from queue", name)
        value = self.get()
        print("%s:got %d from queue", name, value)
        return value

    def set_message(self, value, name):
        print("%s:about to add %d to queue", name, value)
        self.put(value)
        print("%s:added %d to queue", name, value)


def producer(pipeline):
    """Producer gửi các message đi"""
    # Chỉ chạy khi event chưa đc trigger
    while not event.is_set():
        message = random.randint(1, 101)
        print(f"Producer got message: {message}")
        pipeline.set_message(message, "Producer")

    # Send a sentinel message to tell consumer we're done
    pipeline.set_message(SENTINEL, "Producer")


def consumer(pipeline):
    """Consumer nhận và lưu giá trị từ msg."""
    message = 0
    # Chỉ chạy khi event chưa đc trigger hoặc vẫn còn msg trong Pipeline
    while not event.is_set() or not pipeline.empty():
        message = pipeline.get_message("Consumer")
        if message is not SENTINEL:
            print(f"Consumer storing message: {message}")


if __name__ == "__main__":
    pipeline = Pipeline()

    # Event, 1 công cụ để quản lí các thread hiệu quả hơn
    event = threading.Event()
    with concurrent.futures.ThreadPoolExecutor(max_workers=2) as executor:
        executor.submit(producer, pipeline, event)
        executor.submit(consumer, pipeline, event)
        time.sleep(0.1)
        print("Set event")
        event.set()  # Trigger event

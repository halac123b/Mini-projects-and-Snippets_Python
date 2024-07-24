import concurrent.futures
import time


def thread_function(name):
    print(f"Start thread {name}")
    time.sleep(2)
    print(f"End thread {name}")


# ThreadPoolExecutor: Context manager giúp quản lí nhiều thread cùng lúc
## max_workers: số thread cùng chạy trong context
## Sau khi ra khỏi with(), sẽ tự động gọi join() cho từng thread theo thứ tự đc thêm vào list
## max_workers: số thread tối đa chạy trong context
with concurrent.futures.ThreadPoolExecutor(max_workers=3) as executor:
    # map(): tạo 1 lúc nhiều thread, pass vào 1 generator để tạo arg cho thread
    ## Map hàm vào thread, dùng range(3) sẽ generate ra 3 thread
    executor.map(thread_function, range(3))
    # NOTE: đây là cách tốt hơn để quản lí nhiều thread khi join() tự động gọi, nhưng vẫn tồn tại hạn chế là không control đc schedule chạy của OS

    # Tạo 1 thread đơn
    executor.submit(thread_function, 4)

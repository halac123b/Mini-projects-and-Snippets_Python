import time

# Thời gian từ lúc January 1, 1970
## Tùy vào system mà code chạy, kết quả có thể ở dạng milisecond hoặc second
## Nếu system time bị thay đổi, kết quả cũng đổi theo
print(time.time())

# Tạm dừng chương trình trong 2s
time.sleep(2)

# Giống time.time() nhưng độ chính xác cao hơn nhiều (và nặng hơn)
time_start = time.perf_counter()

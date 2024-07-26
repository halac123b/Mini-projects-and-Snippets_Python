import logging

# Đặt cấu trúc của câu log cho 1 log level cụ thể
## level: đag set cho level INFO
## format: cấu trúc, theo các tên định nghĩa sẵn (time, level, nội dung log)
## datefmt: format của date dùng cho (asctime)
format = "%(asctime)s - %(levelname)s - %(message)s"
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
    datefmt="%H:%M:%S",
)
# Log thông tin ở level INFO
logging.info("This is an INFO log")
logging.debug("This is a DEBUG msg")

# getLogger(): trong chương trình có thể chứa nhiều logger, hàm này giúp get 1 logger theo tên
## Nếu k pass tên, return root logger
# setLevel(): level của các log đc in ra console
## Có các level từ thấp > cao: info → debug
logging.getLogger().setLevel(logging.DEBUG)

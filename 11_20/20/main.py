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

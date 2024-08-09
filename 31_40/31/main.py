import inspect


def log_message(message):
    # Get frame hiện tại trong call stack
    ## Call stack: stack chứa thông tin về các hàm đã đc gọi trong chương trình, khi hàm return sẽ ra khỏi stack
    # f_back: dịch chuyển về trc 1 frame (tức hàm trc khi gọi hàm này)
    frame = inspect.currentframe().f_back
    # f_code: Code obj, chứa các metadata về hàm đc gọi trong stack
    ## co_filename: str, tên file chứa hàm đc gọi
    filename = frame.f_code.co_filename.split("\\")[-1]
    # f_lineno: index của hàng mà code đc gọi
    line_number = frame.f_lineno
    print(f"[{filename}:{line_number}] {message}")


def example_function():
    log_message("This is a debug message")


example_function()

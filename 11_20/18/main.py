import trio


async def async_double(x):
    print("Before")
    await trio.sleep(3)  # giống time.sleep()


def nor_func():
    # Simplest feature of trio - cho phép gọi hàm async trong hàm thường
    trio.run(async_double, 3)


nor_func()

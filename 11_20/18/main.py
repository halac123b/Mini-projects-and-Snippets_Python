import trio
import tracer


async def child1():
    print("Start child1")
    await trio.sleep(1)  # giống time.sleep()
    print("End child1")


async def child2():
    print("Start child2")
    await trio.sleep(1)
    print("End child2")


def nor_func():
    # Simplest feature of trio - cho phép gọi hàm async trong hàm thường
    trio.run(child1, 3)


async def parent():
    # nursery: 1 dạng context manager để quản lí cùng lúc nhiều hàm async (giống concurrent.futures.ThreadPoolExecutor với thread)
    # Với các lệnh with trong đó có hàm async, cần phải gọi async with
    async with trio.open_nursery() as nursery:
        # Chạy 1 hàm async, nhưng return để quay về hàm chính ngay
        ## Phải khi hàm chính chạy hết with thì mới đợi để async chạy hết
        nursery.start_soon(child1)
        nursery.start_soon(child2)


# Gọi hàm kèm theo instruments để trace
trio.run(parent, instruments=[tracer.Tracer()])

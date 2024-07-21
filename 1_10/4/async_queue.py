import asyncio
import os
import random
import time
import itertools


async def makeitem(size: int = 5) -> str:
    # Tạo random 1 string có độ dài size
    # Sau đó chuyên thành 1 string dạng hex
    return os.urandom(size).hex()


async def randsleep(caller=None) -> None:
    i = random.randint(0, 10)
    if caller:
        print(f"{caller} sleeping for {i} seconds.")
    await asyncio.sleep(i)


# Hàm để sản xuất ra task
async def produce(name: int, q: asyncio.Queue) -> None:
    n = random.randint(0, 10)
    # itertools.repeat(): tạo 1 iterator obj (obj có thể duyệt qua các item), lặp lại 1 giá trị n lần
    for _ in itertools.repeat(None, n):  # Synchronous loop for each single producer
        await randsleep(caller=f"Producer {name}")
        i = await makeitem()
        t = time.perf_counter()
        # Add 1 task async vào queue, gồm hàm và thời gian bắt đầu chạy hàm
        await q.put((i, t))
        print(f"Producer {name} added <{i}> to queue.")


# Hàm xử lí task
async def consume(name: int, q: asyncio.Queue) -> None:
    while True:
        await randsleep(caller=f"Consumer {name}")
        # Lấy 1 task async ra khỏi queue
        i, t = await q.get()
        now = time.perf_counter()
        print(f"Consumer {name} got element <{i}>" f" in {now-t:0.5f} seconds.")
        # Đánh dấu task đã hoàn thành, xóa task khỏi queue
        q.task_done()


async def main(nprod: int, ncon: int):
    q = asyncio.Queue()
    # Tạo ra 2 task để tạo và xử lí các task IO
    producers = [asyncio.create_task(produce(n, q)) for n in range(nprod)]
    consumers = [asyncio.create_task(consume(n, q)) for n in range(ncon)]
    await asyncio.gather(*producers)

    await q.join()  # Implicitly awaits consumers, too
    for c in consumers:
        c.cancel()


if __name__ == "__main__":
    import argparse

    random.seed(444)
    parser = argparse.ArgumentParser()
    parser.add_argument("-p", "--nprod", type=int, default=5)
    parser.add_argument("-c", "--ncon", type=int, default=10)
    ns = parser.parse_args()
    start = time.perf_counter()
    asyncio.run(main(**ns.__dict__))
    elapsed = time.perf_counter() - start
    print(f"Program completed in {elapsed:0.5f} seconds.")

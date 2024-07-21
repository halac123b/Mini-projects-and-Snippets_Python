#!/usr/bin/env python3

import asyncio
import time


# Hàm async, chứa code chạy bất đồng bộ, hay 1 coroutine
async def count():
    print("One")
    # Khi gọi await, code này trả lại quyền điều khiển cho event loop, và chuyển sang chạy code khác
    await asyncio.sleep(1)
    print("Two")


async def main():
    await asyncio.gather(count(), count(), count())


if __name__ == "__main__":
    s = time.perf_counter()
    asyncio.run(main())
    elapsed = time.perf_counter() - s
    print(f"{__file__} executed in {elapsed:0.2f} seconds.")

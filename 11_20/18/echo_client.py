import sys
import trio

# Số port bất kì, trog khoảng 1024 and 65535
## K đc sử dụng bởi chương trình khác
## Trùng với port của server
PORT = 12345


async def sender(client_stream):
    print("sender: started!")
    while True:
        # A byte string
        data = b"async can sometimes be confusing, but I believe in you!"
        # In giá trị của data dưới dạng raw string (có dấu nháy, escape sequence)
        print(f"sender: sending {data!r}")
        # Send data qua TCP Stream
        await client_stream.send_all(data)
        await trio.sleep(1)


async def receiver(client_stream):
    """Nhận data đc gửi từ sender"""
    print("receiver: started!")
    async for data in client_stream:
        print(f"receiver: got data {data!r}")
    print("receiver: connection closed")
    sys.exit()


async def parent():
    print(f"parent: connecting to 127.0.0.1:{PORT}")
    # Open 1 TCP steam đến IP và host xác định
    client_stream = await trio.open_tcp_stream("127.0.0.1", PORT)
    async with client_stream:
        async with trio.open_nursery() as nursery:
            print("parent: spawning sender...")
            nursery.start_soon(sender, client_stream)

            print("parent: spawning receiver...")
            nursery.start_soon(receiver, client_stream)


trio.run(parent)

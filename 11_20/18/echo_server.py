import trio
import itertools

PORT = 12345
CONNECTION_COUNTER = itertools.count()


async def echo_server(server_stream):
    # Assign each connection a unique number to make our debug prints easier
    # to understand when there are multiple simultaneous connections.
    ident = next(CONNECTION_COUNTER)
    print(f"echo_server {ident}: started")
    try:
        async for data in server_stream:  # Lấy data đc gửi lên từ client qua stream
            print(f"echo_server {ident}: received data {data!r}")
            await server_stream.send_all(data)
        print(f"echo_server {ident}: connection closed")
    except Exception as exc:
        print(f"echo_server {ident}: crashed: {exc!r}")


async def main():
    # Chạy TCP server với Trio
    ## Tạo nursery bên trong, qua đó có thể handle đc nhiều msg từ client cùng lúc
    ## echo_server: hàm handle msg, chứa arg là 1 TCP Stream, khi có msg đến, tự start 1 async task bằng hàm đó
    await trio.serve_tcp(echo_server, PORT)


trio.run(main)

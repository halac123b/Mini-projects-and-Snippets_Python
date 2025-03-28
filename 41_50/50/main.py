import gipc

# Tạo 1 pipe với 2 đầu endpoint
## duplex: cả 2 đầu đều có quyền send, receive
## encode: hàm biến đổi trc khi data đc gửi đi
pipe_parent, pipe_child = gipc.pipe(
    duplex=True,
    encoder=lambda x: x + "2",
)

def myFunc(arg1):
    print(arg1)

# Start process mới và chạy hàm myFunc() bên trog
process = gipc.start_process(
            target=myFunc,
            kwargs={
                'arg1': 1
            }
        )

# Gửi data vào 1 pipe, data này sẽ đi qua hàm encoder, rồi đến phía pipe nhận
pipe_child.put(1)
# Get data đc gửi từ pipe_child, theo thứ tự FIFO, nào đến trc thì lấy trc
## Nếu k set timeout, pipe sẽ chờ hoài đến khi có data
pipe_parent.get()
pipe_parent.get(1)  # Chỉ chờ tối đa 1s
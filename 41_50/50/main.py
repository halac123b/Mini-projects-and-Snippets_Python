import gipc

# Tạo 1 pipe với 2 đầu endpoint
## duplex: cả 2 đầu đều có quyền send, receive
## encode: hàm biến đổi trc khi data đc gửi đi
pipe_parent, pipe_child = gipc.pipe(
    duplex=True,
    encoder=lambda x: x + "2",
)

def myFunc(arg1):
    pass

# Start process mới và chạy hàm myFunc() bên trog
process = gipc.start_process(
            target=myFunc,
            kwargs={
                'arg1': 1
            }
        )


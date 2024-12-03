import socket

# Tạo 1 socket để trao đổi data qua lại với nhau
## AF_UNIX: Address family của UNIX, tức đây là socket nội bộ giữa các process, chỉ dùng đc cho UNIX, k Windows
## AF_INET6: socket với các máy khác trên mạng
## SOCK_STREAM: protocol TCP
listener = socket.socket(socket.AF_UNIX, socket.SOCK_STREAM)

# Bind socket vào 1 file, folder, folder có thể giao tiếp với các socket local khác
## Chỉ dùng cho socket local
listener.bind("path/to/find")

# In case INET socket, bind bằng cặp IP, Port
# listener.bind((host, port))

# Setting cho socket (chỉ dùng cho INET)
## IPPROTO_TCP: đang set cho các socket TCP layer
## TCP_CORK: 1 algo quy định khi gửi data
### Data sẽ đc lưu trong buffer thành các gói lớn rồi mới gửi đi thay vì gửi lẻ tẻ (chỉ có trên Unix)
listener.setsockopt(socket.IPPROTO_TCP, socket.TCP_CORK, 1)

# SOL_SOCKET: Socket Option Level, tức chỉ setting cho đúng socket đó
## Lệnh ở trên là set cho toàn bộ protocol
# SO_REUSEADDR: cho phép bind External socket đến 1 port đã đc cấp phát cho 1 socket trc đó vừa đc sử dụng xong, mà k cần lặp lại quá trình release resource rồi cấp phát lại
listener.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

# Open socket with max 10 connection in queue
listener.listen(10)
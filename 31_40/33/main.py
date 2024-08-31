import gevent

urls = ["www.google.com", "www.example.com", "www.python.org"]

# Tạo 3 greenlet
# spawn(): tạo và chạy 1 greenlet (a lightweight, cooperative thread)
## Arg: hàm để thread chạy
# socket.gethostbyname(url): từ url lấy địa chỉ IPv4
## Hàm này override lại hàm gốc của socket package (hàm cũ là block, hàm mới non-block, khi gọi chương trình vẫn tiếp tục chạy)
jobs = [gevent.spawn(gevent.socket.gethostbyname, url) for url in urls]

# Giống join() bên thread khi main thread sẽ chờ để các thread con kết thúc hết
## timeout: nếu đợi lâu hơn mà vẫn chạy chưa xong thì trở lại thread chính
_ = gevent.joinall(jobs, timeout=2)
# greenlet.value: giá trị return của hàm
print([job.value for job in jobs])

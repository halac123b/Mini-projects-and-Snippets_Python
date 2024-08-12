import gevent
import requests

# Monkey patching module, có chức năng đóng gói các hàm từ std lib có sẵn sang dạng greenlet
## Giúp các hàm k liên quan greenlet vẫn chạy trog greenlet đc

# patch_all(): thao tác đầu tiên để patch các std lib
gevent.monkey.patch_all()

urls = ["https://www.google.com/", "https://www.apple.com/", "https://www.python.org/"]


def print_head(url):
    print("Starting %s" % url)
    data = requests.get(url).text
    print("%s: %s bytes: %r" % (url, len(data), data[:50]))


jobs = [gevent.spawn(print_head, _url) for _url in urls]

# Bên cạnh joinall(), đây là hàm khác để chờ greenlet đa dạng hơn
## Thay vì chờ toàn bộ, có thể set điều kiện
## count: nếu đủ số lượng greenlet chạy xong, k chờ nữa
gevent.wait(jobs, count=1)

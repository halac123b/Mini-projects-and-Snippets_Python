from gevent.lock import RLock

# Tạo 1 reentrant lock cho greenlet (lock cho phép cùng 1 greenlet đc accquire nhiều lần liên tục)
## Sau đó greenlet phải release lại đúng số lần đã accquire để release hết
buffer_lock = RLock()
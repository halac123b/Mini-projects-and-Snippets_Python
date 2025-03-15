import base64

# Chuyển string thành dạng b64-bytes
encoded = base64.b64encode("Hello, world!".encode())

# string.encode(): chuyển string sang dạng b64-bytes
# b64decode(): chuyển b-64 sang original binari data
encoded = base64.b64decode(encoded)
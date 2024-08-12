import requests

# Có thể gọi trực tiếp hàm của get()
## Return Response object
## Response.text: nội dung dạng text của response
## Đây là hàm block, nên chương trình sẽ bị ngưng lại để chờ hàm này chạy xog
data = requests.get("https://www.google.com/").text

print(data)

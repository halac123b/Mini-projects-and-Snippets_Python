import pickle

x = 2
# Serialize 1 obj thành 1 byte stream để có thể lưu dạng file
## 5: protocol đc dùng, đây là ver mới nhất từ Python 3.8
byteStream = pickle.dumps(x, 5)

# Deserialize 1 byte stream (đã đc pickle trc đó) thành 1 obj
string = pickle.loads(byteStream)
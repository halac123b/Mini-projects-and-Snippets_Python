import redis

# Connect đến Redis local, đc return 1 byte data
## decode_responses: decode bytedata thành string
redis_db = redis.Redis(host='localhost', port=6379, decode_responses=True)

# Set and get simple data
## Data đc lưu ở top-level của database
redis_db.set('name', 'Alice')
print(redis_db.get('name')) # Alice

# Data gồm các key-value thay vì lưu top-level như ở trên sẽ lưu trong 1 tập nhỏ hơn gọi là hash
redis_db.hset('user-session:123', mapping={
    'name': 'John',
    "surname": 'Smith',
    "company": 'Redis',
    "age": 29
})
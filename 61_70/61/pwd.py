import pwd
# Package tương tác với Password database trên Linux (list các user, thông tin login)

# Get PW theo tên user
data = pwd.getpwnam("user_name")
# Get bằng 1 UserId
data = pwd.getpwuid(12)
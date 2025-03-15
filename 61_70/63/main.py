import syslog

# Chuẩn bị mở log với facility là LOG_AUTH
## Tuỳ vào facility mà log sẽ đc ghi vào file tương ứng
syslog.openlog(facility=syslog.LOG_AUTH)

# Ghi log vào log file của Unix OS
## LOG_NOTICE: mức độ của log
syslog.syslog(syslog.LOG_NOTICE, "User login detected from system")
import sqlite3

# Open a connection to the database file
connection = sqlite3.connect("./autoblog.db")
# Taọ cursor object, trog SQL cursor là con trỏ giúp chạy cách SQL query
cursor = connection.cursor()
# Chạy 1 lệnh SQL
cursor.execute("SQL query")
# Commit thay đổi nếu có sau khi chạy lệnh SQL, nếu k change sẽ mất khi kết thúc chương trình
connection.commit()

# Close the connection
connection.close()
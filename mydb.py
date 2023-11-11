import mysql.connector

# kết nối đến mysql 
data_base = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="1166",
    auth_plugin='mysql_native_password'
)
cursor_object = data_base.cursor()

print("Kết nối thành công")

# tạo database "library"
cursor_object.execute("CREATE DATABASE library")
print("Tạo database thành công")

# xóa database
# cursor_object.execute("DROP DATABASE library")
# print("Xóa database thành công")
    
data_base.close()
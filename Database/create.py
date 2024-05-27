
import mysql.connector
 
mydb = mysql.connector.connect(
    host = "localhost",
    user = "admin",
    password = "mysql"
)

print(mydb)

cursor = mydb.cursor()
cursor.execute("CREATE DATABASE db")
cursor.execute("SHOW DATABASES")
 
for x in cursor:
  print(x)
  
'''
<mysql.connector.connection_cext.CMySQLConnection object at 0x00000263EC975D00>
('db',)
('deepteck',)
('demo',)
('information_schema',)
('labs',)
('moviedatabasemanagementsystem',)
('moviesdatabasemanagementsystem',)
('mysql',)
('performance_schema',)
('sakila',)
('sms',)
('studentmanagementsystem',)
('sys',)
('world',)
'''
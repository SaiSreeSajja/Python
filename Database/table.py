import mysql.connector
 
mydb = mysql.connector.connect(
    host = "localhost",
    user = "admin",
    password = "mysql",
    database='db'
)

print(mydb)

cursor = mydb.cursor()
cursor.execute("CREATE TABLE student (roll int,name VARCHAR(20),marks int)")
cursor.execute("SHOW TABLES")
 
for x in cursor:
  print(x)
  
'''
<mysql.connector.connection_cext.CMySQLConnection object at 0x000001431D2BEDC0>
('student',)
'''
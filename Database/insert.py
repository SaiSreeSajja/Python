import mysql.connector
 
 
mydb = mysql.connector.connect(
  host = "localhost",
  user = "admin",
  password = "mysql",
  database = "db"
) 
 
mycursor = mydb.cursor()
sql = "INSERT INTO student (roll,name,marks) VALUES (%s , %s , %s)"
val = (122,"Sai", 85)
 
mycursor.execute(sql, val)
mydb.commit()
 
print(mycursor.rowcount, "details inserted")
 
mydb.close()
'''
1 details inserted
'''
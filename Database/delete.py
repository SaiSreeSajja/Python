import mysql.connector
 
 
mydb = mysql.connector.connect(
  host = "localhost",
  user = "admin",
  password = "mysql",
  database = "db"
) 
 
mycursor = mydb.cursor()
mycursor.execute("DELETE FROM STUDENT WHERE NAME = 'Sai'")
mydb.commit()
 
print(mycursor.rowcount, "details deleted")
 
mydb.close()

'''
1 details deleted
'''
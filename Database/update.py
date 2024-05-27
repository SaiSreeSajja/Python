import mysql.connector
 
 
mydb = mysql.connector.connect(
  host = "localhost",
  user = "admin",
  password = "mysql",
  database = "db"
) 
 
mycursor = mydb.cursor()
mycursor.execute("UPDATE STUDENT SET marks=90 WHERE NAME = 'Sai'")
mydb.commit()
 
print(mycursor.rowcount, "details updated")
 
mydb.close()

'''
1 details updated
'''
import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  passwd="afroz123",
  database="proplayer"
)

mycursor = mydb.cursor()

sql = "UPDATE customers SET address = %s WHERE address = %s"
val = ("Valley 345", "Canyon 123")

mycursor.execute(sql, val)

mydb.commit()

print(mycursor.rowcount, "record(s) affected") 
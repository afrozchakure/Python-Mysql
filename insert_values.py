

import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  passwd="afroz123",
  database="proplayer"
)

mycursor = mydb.cursor()

sql = "INSERT INTO customers (name, address) VALUES (%s, %s);"

val = ("John", "Highway 21")

mycursor.execute(sql, val)   

mydb.commit()  # It is required to make changes otherwise no changes will be made

print(mycursor.rowcount, "Record Inserted.")
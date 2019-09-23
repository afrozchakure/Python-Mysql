# Returning the last row id of a table

import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  passwd="afroz123",
  database="proplayer"
)

mycursor = mydb.cursor()

sql = "INSERT INTO customers (name, address) VALUES (%s, %s);"

val = ("Michele", "Blue Village")

mycursor.execute(sql, val)

mydb.commit()

print("1 record inserted, ID:", mycursor.lastrowid)

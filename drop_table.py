import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  passwd="afroz123",
  database="proplayer"
)

mycursor = mydb.cursor()

# sql = "DROP TABLE employee"  # Droping a single table

# you can use the IF EXISTS keyword to avoid getting an error.
sql = "DROP TABLE IF EXISTs employee"  # Dropping a table if it exists

mycursor.execute(sql) 
# Deleting a record from a database

import mysql.connector

mydb = mysql.connector.connect(
    host = "localhost",
    user = "root",
    passwd = "afroz123",
    database = "proplayer"
)

mycursor = mydb.cursor()

sql = "DELETE FROM customers WHERE address = 'Mountain 21'"

# sql = "SELECT * FROM customers"

mycursor.execute(sql)

# The mydb.commit() method is required to make changes, otherwise no changes will be made to the table
# It is not needed when we are just displaying the rows
mydb.commit()

print(mycursor.rowcount, "record(s) deleted")


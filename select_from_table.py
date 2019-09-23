# Using the SELECT statement

import mysql.connector

mydb = mysql.connector.connect(
    host = "localhost",
    user = "root",
    passwd = "afroz123",
    database = "proplayer"
)

mycursor = mydb.cursor()  # Creates an object of mydb

mycursor.execute("SELECT * FROM customers;")

myresult = mycursor.fetchall()  # Fetches all rows from the last executed statement (returns a list)

for x in myresult:  # Used to display all the rows within the myresult list
    print(x)

print(type(myresult))  # It is a list of values

print(myresult) # Displays the list of values
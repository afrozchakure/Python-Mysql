# Using the SELECT statement

import mysql.connector

mydb = mysql.connector.connect(
    host = "localhost",
    user = "root",
    passwd = "afroz123",
    database = "proplayer"
)

mycursor = mydb.cursor()  # Creates an object of mydb


### For selecting all the rows form a table

# mycursor.execute("SELECT * FROM customers;")   # Displays all the rows of the table
# myresult = mycursor.fetchall()  # Fetches all rows from the last executed statement (returns a list)
# for x in myresult:  # Used to display all the rows within the myresult list
#     print(x)
# print(type(myresult))  # It is a list of values


### For selecting a single row from a table with specified columns 

mycursor.execute("SELECT name, address FROM customers")  # Displays only the specified columns of the table
myresult = mycursor.fetchone()  # It will return only  the first row of the result
print(myresult) # Displays the list of values
print(type(myresult))  # It is a tuple with single value





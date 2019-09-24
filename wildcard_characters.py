# Select the records that starts, includes, or ends with a given letter or phrase

import mysql.connector

mydb = mysql.connector.connect(
    host = "localhost",
    user = "root",
    passwd = "afroz123",
    database = "proplayer"
)

mycursor = mydb.cursor()

sql = "SELECT * FROM customers WHERE address LIKE '%way%'"  # Select the records where the address contains the word "way"

mycursor.execute(sql)

myresult = mycursor.fetchall()

for x in myresult:
    print(x)
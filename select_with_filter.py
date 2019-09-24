import mysql.connector

mydb = mysql.connector.connect(
    host = "localhost",
    user = "root",
    passwd = "afroz123",
    database = "proplayer"
)

mycursor = mydb.cursor()   # Creating an object of mydb

sql = "SELECT * FROM customers WHERE address = 'Park Lane 38'"  # Selecting with a where clause

mycursor.execute(sql)

myresult = mycursor.fetchall()  # Fetches all rows with following entries

for x in myresult:
    print(x)
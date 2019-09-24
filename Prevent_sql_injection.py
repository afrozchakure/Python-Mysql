# When query values are provided by the user, you should escape the values.

# This is to prevent SQL injections, which is a common web hacking technique 
# to destroy or misuse your database.

import mysql.connector

mydb = mysql.connector.connect(
    host = "localhost",
    user = "root",
    passwd = "afroz123",
    database = "proplayer"
)

mycursor = mydb.cursor()

sql = "SELECT * FROM customers WHERE address = %s"  # Escape query values by using the placeholder %s method

adr = ("Yellow Garden 2", )

mycursor.execute(sql, adr)

myresult = mycursor.fetchall()

for x in myresult:
    print(x)
# It is considered a good practice to escape the values 
# of any query, also in delete statements.

import mysql.connector

mydb = mysql.connector.connect(
    host = "localhost",
    user = "root",
    passwd = "afroz123",
    database = "proplayer"
)

mycursor = mydb.cursor()

sql = "DELETE FROM customers WHERE address = %s"

adr = ("Yellow Garden 2", )

mycursor.execute(sql, adr)

mydb.commit()

print(mycursor.rowcount, "record(s) deleted")
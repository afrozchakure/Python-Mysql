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
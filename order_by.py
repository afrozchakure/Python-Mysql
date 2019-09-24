import mysql.connector

mydb = mysql.connector.connect(
    host = "localhost",
    user = "root",
    passwd = "afroz123",
    database = "proplayer"
)

mycursor = mydb.cursor()

# sql = "SELECT * FROM customers ORDER BY name"  # It sorts the result in ascending order by default
sql = "SELECT * FROM customers ORDER BY name DESC"  # It sorts the result in descending order

mycursor.execute(sql)

myresult = mycursor.fetchall()

for x in myresult:
    print(x)


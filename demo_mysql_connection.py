import mysql.connector


# Making the connection with the database
mydb = mysql.connector.connect(
    host = 'localhost',
    user = 'root',
    passwd = 'afroz123',
)

mycursor = mydb.cursor()

# mycursor.execute("CREATE DATABASE proplayer")  # Creating a database proplayer

mycursor.execute("SHOW DATABASES")  # Displaying the available databases

for x in mycursor:
    print(x)
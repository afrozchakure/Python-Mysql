import mysql.connector


# Making the connection with the database
mydb = mysql.connector.connect(
    host = 'localhost',
    user = 'root',
    passwd = 'afroz123',
    database = "proplayer"
)

mycursor = mydb.cursor()

# mycursor.execute("CREATE TABLE customers (name VARCHAR(255), address VARCHAR(255));")  # Creating a table in Mysql
# mycursor.execute("SHOW TABLES;")
mycursor.execute("ALTER TABLE customers ADD COLUMN id INT AUTO_INCREMENT PRIMARY KEY;")


# for x in mycursor:  # It iterates over whatever is stored in mycursor object
#     print(x)
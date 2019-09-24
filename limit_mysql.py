import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  passwd="afroz123",
  database="proplayer"
)

mycursor = mydb.cursor()

# Selects the first five records in the "customers" table
# mycursor.execute("SELECT * FROM customers LIMIT 5")  # Uncomment to execute

# If you want to return five records, starting from the third record, we can use the 'OFFSET' keyword
mycursor.execute("SELECT * FROM customers LIMIT 5 OFFSET 2")  

myresult = mycursor.fetchall()

for x in myresult:
    print(x)
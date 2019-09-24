# Both JOIN and INNER JOIN both give similar results

import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  passwd="afroz123",
  database="proplayer"
)

mycursor = mydb.cursor()

# sql = "SELECT \
#     users.name AS user, \
#     products.name as favorite \
#     FROM users \
#     INNER JOIN products ON users.fav = products.id"

# sql = "SELECT \
#     users.name AS user, \
#     products.name AS favorite \
#     FROM users \
#     LEFT JOIN products ON users.fav = products.id"  # It displays all the values of table that comes after 'FROM'


sql = "SELECT \
    users.name AS user, \
    products.name AS favorite \
    FROM users \
    RIGHT JOIN products ON users.fav = products.id"

mycursor.execute(sql)

myresult = mycursor.fetchall()

for x in myresult:
    print(x)

# Hannah and Michael, who have no favorite product, 
# are not included in the result.
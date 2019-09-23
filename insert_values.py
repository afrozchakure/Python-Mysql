

import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  passwd="afroz123",
  database="proplayer"
)

mycursor = mydb.cursor()

sql = "INSERT INTO customers (name, address) VALUES (%s, %s);"

### For Inserting a single row in a table

# val = ("John", "Highway 21")

# mycursor.execute(sql, val)  # Use it for inserting a single row in database

# print(mycursor.rowcount, "Record Inserted.")

### For Inserting multiple rows in a Table

val = [
  ('Peter', 'Lowstreet 4'),
  ('Amy', 'Apple st 652'),
  ('Hannah', 'Mountain 21'),
  ('Michael', 'Valley 345'),
  ('Sandy', 'Ocean blvd 2'),
  ('Betty', 'Green Grass 1'),
  ('Richard', 'Sky st 331'),
  ('Susan', 'One way 98'),
  ('Vicky', 'Yellow Garden 2'),
  ('Ben', 'Park Lane 38'),
  ('William', 'Central st 954'),
  ('Chuck', 'Main Road 989'),
  ('Viola', 'Sideway 1633')
]

mycursor.executemany(sql, val)

mydb.commit()  # It is required to make changes otherwise no changes will be made


print(mycursor.rowcount, "was inserted.")
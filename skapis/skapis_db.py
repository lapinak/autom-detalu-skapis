import mysql.connector

mydb = mysql.connector.connect(
  host="127.0.0.1",
  user=
  password=
  database=
)

mycursor = mydb.cursor()

mycursor.execute("CREATE TABLE IF NOT EXISTS skapis (id INT AUTO_INCREMENT PRIMARY KEY, name varchar(255) NOT NULL, count int NOT NULL, total_weight float NOT NULL, added_by varchar(255) NOT NULL, date datetime NOT NULL)")

mydb.commit()

print(mycursor.rowcount, " rows were inserted!")

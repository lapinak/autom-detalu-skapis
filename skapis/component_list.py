import mysql.connector


#Requires to fill in your DB connection data
mydb = mysql.connector.connect(
  host=
  user=
  password=
  database=
)

mycursor = mydb.cursor()

def create_base():
  mycursor.execute("CREATE TABLE IF NOT EXISTS components (id INT AUTO_INCREMENT PRIMARY KEY, name varchar(255) NOT NULL, weight float NOT NULL)")

  sql = "INSERT INTO components (name, weight) VALUES (%s, %s)"
  val = [
    ('resistor', 0.25),
    ('capacitor', 0.75),
    ('button', 1.63),
    ('diode', 1.12),
    ('RGB', 2.01),
    ('transistor', 0.46),
    ('connector', 3.03)
  ]

  mycursor.executemany(sql, val)

  mydb.commit()



print(mycursor.rowcount, " rows were inserted.")

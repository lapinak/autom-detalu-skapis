import mysql.connector

mydb = mysql.connector.connect(
  host="127.0.0.1",
  user="asteroids_user_s18",
  password="Yoursuperpassword_s18",
  database="asteroids_s18"
)

mycursor = mydb.cursor()

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

print(mycursor.rowcount, "was inserted.")
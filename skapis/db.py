import mysql.connector

mydb = mysql.connector.connect(
  host="127.0.0.1",
  user="asteroids_user_s18",
  password="Yoursuperpassword_s18",
  database="asteroids_s18"
)

mycursor = mydb.cursor()

mycursor.execute("CREATE TABLE components (id INT AUTO_INCREMENT PRIMARY KEY, name varchar(255) NOT NULL, weight float NOT NULL)")
import mysql.connector

mydb = mysql.connector.connect(
  host="127.0.0.1",
  user="asteroids_user_s18",
  password="Yoursuperpassword_s18",
  database="asteroids_s18"
)

mycursor = mydb.cursor()



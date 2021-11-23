import os
import mysql.connector
import component_list
import skapis_db

from configparser import ConfigParser

config = ConfigParser()
config.read('config.ini')

assert config.has_option('mysql_config', 'mysql_host') == True
assert config.has_option('mysql_config', 'mysql_db') == True
assert config.has_option('mysql_config', 'mysql_user') == True
assert config.has_option('mysql_config', 'mysql_pass') == True

mysql_config_mysql_host = config.get('mysql_config', 'mysql_host')
mysql_config_mysql_db = config.get('mysql_config', 'mysql_db')
mysql_config_mysql_user = config.get('mysql_config', 'mysql_user')
mysql_config_mysql_pass = config.get('mysql_config', 'mysql_pass')
connection = mysql.connector.connect(host=mysql_config_mysql_host, database=mysql_config_mysql_db,
                                     user=mysql_config_mysql_user, password=mysql_config_mysql_pass)
assert connection.is_connected() == True

print("Component database test")

print("┌--------------------------┐")
print(" ")
print("Checking if the Component database exists")

connection = None
connected = False


def init_db():
    global connection
    connection = mysql.connector.connect(host=mysql_config_mysql_host, database=mysql_config_mysql_db,
                                         user=mysql_config_mysql_user, password=mysql_config_mysql_pass)


init_db()

component_list.create_base()

def get_cursor():
    global connection
    try:
        connection.ping(reconnect=True, attempts=1, delay=0)
        connection.commit()
    except mysql.connector.Error as err:
        print("No connection to db " + str(err))
        connection = init_db()
        connection.commit()
    return connection.cursor()

print("Printing the data from database")
cursor = get_cursor()
cursor.execute("SELECT * FROM components") == True

for i in cursor:
    print(i)

print("Test successful")
print(" ")
print("└--------------------------┘")
import os
import mysql.connector

from datetime import datetime
from configparser import ConfigParser

print("Configuration file test")

print("┌--------------------------┐")
print("Checking for a config file")
assert os.path.isfile("config.ini") == True
print("Test successful")
print("└--------------------------┘")

# Opening the configuration file
config = ConfigParser()
config.read('config.ini')

# Checking if all MYSQL related config options are present in the config file
print("┌--------------------------┐")
print("Checking if config can read MYSQL parameters")
assert config.has_option('mysql_config', 'mysql_host') == True
assert config.has_option('mysql_config', 'mysql_db') == True
assert config.has_option('mysql_config', 'mysql_user') == True
assert config.has_option('mysql_config', 'mysql_pass') == True
print("Test successful")
print("└--------------------------┘")

# Checking if possible to connect to MySQL with the existing config options
print("┌--------------------------┐")
print("Checking MYSQL connectivity")
mysql_config_mysql_host = config.get('mysql_config', 'mysql_host')
mysql_config_mysql_db = config.get('mysql_config', 'mysql_db')
mysql_config_mysql_user = config.get('mysql_config', 'mysql_user')
mysql_config_mysql_pass = config.get('mysql_config', 'mysql_pass')
connection = mysql.connector.connect(host=mysql_config_mysql_host, database=mysql_config_mysql_db, user=mysql_config_mysql_user, password=mysql_config_mysql_pass)
assert connection.is_connected() == True
print("Test successful")
print("└--------------------------┘")
import logging
import logging.config
import random
import getpass
import datetime
import yaml
import mysql.connector

from datetime import datetime
from configparser import ConfigParser
from mysql.connector import Error


# Loading logging configuration
with open('./log_worker.yaml.dev', 'r') as stream:
    config = yaml.safe_load(stream)

logging.config.dictConfig(config)

# Creating logger
logger = logging.getLogger('root')

try:
    config = ConfigParser()
    config.read('config.ini')

    username = config.get('account', 'username')

    mysql_config_mysql_host = config.get('mysql_config', 'mysql_host')
    mysql_config_mysql_db = config.get('mysql_config', 'mysql_db')
    mysql_config_mysql_user = config.get('mysql_config', 'mysql_user')
    mysql_config_mysql_pass = config.get('mysql_config', 'mysql_pass')

except:
    logger.exception('')
logger.info('DONE')

# Reads config.ini file where username and password are stored to either get simple/guest access or 'account access'

connection = None
connected = False


def init_db():
    global connection
    connection = mysql.connector.connect(host=mysql_config_mysql_host, database=mysql_config_mysql_db,
                                         user=mysql_config_mysql_user, password=mysql_config_mysql_pass)


init_db()


def get_cursor():
    global connection
    try:
        connection.ping(reconnect=True, attempts=1, delay=0)
        connection.commit()
    except mysql.connector.Error as err:
        logger.error("No connection to db " + str(err))
        connection = init_db()
        connection.commit()
    return connection.cursor()


def access():
    # Prompts th user to enter their data
    try:
        user = input("Username: ")

        if user == username:
            return True
        else:
            return False
    except:
        logger.debug(
            "Your provided date is not registered, contact the administrator.")


def authorization():
    try:
        print("1. Log in with account ")
        print("2. Continue in guest mode ")
        access_type = input("What access do you wish to have? ")
        if access_type == '1':
            return access()
        elif access_type == '2':
            return
    except:
        logger.error("Something went wrong.")


# Calls out the method

authorization()

total_weight = float(input("Enter the full weight: "))
try:
    query = "select * from components"
    cursor = get_cursor()
    cursor.execute(query)
    components = cursor.fetchall()
    logger.info("Total number of rows in table: ", str(cursor.rowcount))

    inputvalue = str(input("What component did you weight? "))
    temp = False
    for c in components:
        if inputvalue in c:
            temp = True
    if temp:
        logger.info("You're adding " +inputvalue+ " to database")
    else:
        logger.debug("Data Does Not Exist")
except mysql.connector.Error as e:
    print("Error reading data from MySQL table", e)

try:
    one = "select weight from components where name = '"+inputvalue+"'"
    query_two = one
    cursor = get_cursor()
    cursor.execute(query_two)
    record = cursor.fetchone()
    single_weight = float(record[0])
    logger.info("Wight of a single " +inputvalue+ " is " + str(single_weight))
except mysql.connector.Error as error:
    logger.error("Failed to get record from database: {}".format(error))

count = total_weight/single_weight
print("You're adding " +str(count)+ " " +str(inputvalue)+ "'s to the database")
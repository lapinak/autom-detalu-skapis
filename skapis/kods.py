import logging
import logging.config
import random
import getpass
import datetime
import yaml

from datetime import datetime
from configparser import ConfigParser

# Loading logging configuration
with open('./log_worker.yaml.dev', 'r') as stream:
    config = yaml.safe_load(stream)

logging.config.dictConfig(config)

# Creating logger
logger = logging.getLogger('root')

"""
a = random.uniform(0, 500)
b = random.uniform(0, 10)

print(a)
print(b)

skaits = int(a/b)

if (skaits % 10 == 1):
    print("Nodalījumā ir: ", skaits ,"component")
else:
    print("Nodalījumā ir: ", skaits ,"components")
"""

#Reads config.ini file where username and password are stored to either get simple/guest access or 'account access'
def access() :
    try :
        config = ConfigParser()
        config.read('config.ini')

        username = config.get('account', 'username')
        passwd = config.get('account', 'passw')
    except :
        #In case if soemthing has gone wrong with accessing the data in beginning stage there is a print with an error
        logger.error("We can't access the configuration file with your account details.")

    #Prompts th user to enter their data
    try :
        user = input("Username: ")
        passw = getpass.getpass("Password: ")

        if user == username and passw == passwd :
            return True
        else :
            return False
    except :
        logger.debug("Your provided date is not registered, contact the administrator.")

#The actual access method
def authorization() :
    try:
        print("1. Log in with account ")
        print("2. Continue in guest mode ")
        access_type = input("What access do you wish to have? ")
        if access_type == '1' :
            return access()
        elif access_type == '2' :
            return
    except:
        logger.error("Something went wrong.")


#Calls out the method
authorization()

try:
    weight = float(input("Enter the full weight: "))
    component = input("What component did you weight?")
    count = float(weight/3)
    logger.info("You've added ", count, component, " to the database")
except: logger.debug("Make sure you have entered numbers and all the kommas are the dot (.) symobol")

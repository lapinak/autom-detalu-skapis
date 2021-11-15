import random
import getpass

from configparser import ConfigParser

a = random.uniform(0, 500)
b = random.uniform(0, 10)


"""
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
        print("We can't access the configuration file with your account details.")

    #Prompts th user to enter their data
    try :
        user = input("Username: ")
        passw = getpass.getpass("Password: ")

        if user == username and passw == passwd :
            return True
        else :
            return False
    except :
        print("Your provided date is not registered, contact the administrator.")

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
        print("Something went wrong.")

def details() :
    try: 
        full_weight = float(input("Enter the full weight: "))
    except: print("Make sure you have entered numbers and all the kommas are the dot (.) symobl")
    component = input("What component did you weight? ")

#Calls out the method
authorization()
details()




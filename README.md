kods_db.py
The main file for executing the code. This prompts a user input, to either
log in with authorised access or to continue in guest mode to then add data
to a components database.

For this code you will need to install requests, mysql-connector and use
python version 3+

To properly work the code you will need config.ini and log_worker.yaml files.
You can use the ones in this directory and change it to your needed settings.

config.ini file:

[account]
username = your_user

[mysql_config]
mysql_host = 127.0.0.1
mysql_db = db_name
mysql_user = db_user
mysql_pass = db_passw

Run python3 kods_db.py to start the code

#!/bin/bash
secret="/secret_folder"

echo "Script for preparing the development environment"
echo "------------------------------------------------"

echo "Checking if config.ini exists"
if test -f "config.ini"; then
    echo "exists"
else
	echo "Copying config file from secure secret storage"
	cp $HOME$secret/config.ini .
	if [ $? -eq 0 ]; then echo "OK"; else echo "Problem copying config.ini file"; exit 1; fi
fi
echo "------------------------------------------------"

echo "Checking if log_worker.yaml exists"
if test -f "log_worker.yaml"; then
    echo "exists"
else
	echo "Copying log config file from local dev template log_worker.yaml.dev"
	cp log_worker.yaml.dev log_worker.yaml
	if [ $? -eq 0 ]; then echo "OK"; else echo "Problem copying log_worker.yaml file"; exit 1; fi
fi
echo "------------------------------------------------"

echo "Getting python3 executable"
python_exec_loc=$(which python3)
if [ $? -eq 0 ]; then echo "OK"; else echo "Problem getting python3 exec location"; exit 1; fi
echo "$python_exec_loc"
echo "------------------------------------------------"

echo "Running config tests"
$python_exec_loc config_test.py
if [ $? -eq 0 ]; then echo "OK"; else echo "Configuration test FAILED"; exit 1; fi
echo "------------------------------------------------"

echo "Running component database test"
$python_exec_loc db_test.py
if [ $? -eq 0 ]; then echo "OK"; else echo "Component_db test FAILED"; exit 1; fi
echo "------------------------------------------------"

echo "Setting up the main database"
$python_exec_loc skapis_db.py
if [ $? -eq 0 ]; then echo "OK"; else echo "Could not initiate the database"; exit 1; fi
echo "------------------------------------------------"

echo "To start the program, execute:"
echo "$python_exec_loc kods_db.py"
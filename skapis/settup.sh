#!/bin/bash
sec_secret_storage_loc="/secret_folder"

echo "Script for preparing the development environment"
echo "------------------------------------------------"

echo "Checking if config.ini exists in the current working dir -->"
if test -f "config.ini"; then
    echo "exists"
else
	echo "Copying config file from secure secret storage"
	cp $HOME$sec_secret_storage_loc/config.ini .
	if [ $? -eq 0 ]; then echo "OK"; else echo "Problem copying config.ini file"; exit 1; fi
fi
echo "------------------------------------------------"

echo "Checking if log_worker.yaml exists in the current working dir -->"
if test -f "log_worker.yaml"; then
    echo "exists"
else
	echo "Copying log config file from local dev template log_worker.yaml.dev"
	cp log_worker.yaml.dev log_worker.yaml
	if [ $? -eq 0 ]; then echo "OK"; else echo "Problem copying log_worker.yaml file"; exit 1; fi
fi
echo "------------------------------------------------"

echo "Getting python3 executable loc"
python_exec_loc=$(which python3)
if [ $? -eq 0 ]; then echo "OK"; else echo "Problem getting python3 exec location"; exit 1; fi
echo "$python_exec_loc"
echo "------------------------------------------------"

echo "Running config tests"
$python_exec_loc config_test.py
if [ $? -eq 0 ]; then echo "OK"; else echo "Configuration test FAILED"; exit 1; fi
echo "------------------------------------------------"

echo "Running asteroid worker tests"
$python_exec_loc db_test.py
if [ $? -eq 0 ]; then echo "OK"; else echo "Worker test FAILED"; exit 1; fi
echo "------------------------------------------------"

echo "ALL SET UP! YOU ARE READY TO CODE"
echo "to start the program, execute:"
echo "$python_exec_loc worker_2_db.py"
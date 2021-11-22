#!/bin/bash
location="/secret_folder"

echo "Checking if config.ini exists"
if test -f "config.ini"; then
    echo "exists"
else
	echo "Copying config file"
	cp $HOME$location/config.ini .
	if [ $? -eq 0 ]; then echo "OK"; else echo "Problem copying config.ini file"; exit 1; fi
fi
echo "------------------------------------------------"

echo "Checking if log_worker.yaml exists"
if test -f "log_worker.yaml"; then
    echo "exists"
else
	echo "Copying log config file"
	cp log_worker.yaml.dev log_worker.yaml
	if [ $? -eq 0 ]; then echo "OK"; else echo "Problem copying log_worker.yaml file"; exit 1; fi
fi
echo "------------------------------------------------"

echo "Creating component database"
$python_exec_loc component_list.py
if [ $? -eq 0 ]; then echo "OK"; else echo "Database activisation FAILED"; exit 1; fi
echo "------------------------------------------------"

echo "Creating skapis database"
$python_exec_loc component_list.py
if [ $? -eq 0 ]; then echo "OK"; else echo "Database activisation FAILED"; exit 1; fi
echo "------------------------------------------------"

echo "You're all set"
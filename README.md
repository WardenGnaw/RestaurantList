# RestaurantList

[![Build Status](https://travis-ci.org/WardenGnaw/RestaurantList.svg?branch=master)](https://travis-ci.org/WardenGnaw/RestaurantList)

## Requirements
There are the requirements to have this project running. This project uses Python3, virtualenv, flask and MySQL.

### OSX
1. Install [homebrew](https://brew.sh/)
2. Install MySQL
   * ```brew services start mysql```
   * ```mysql_sercure_installation```
   * ```mysql -u root -p```
3. Install python3
   * ```brew install python3```
4. Install virtualenv
   * ```pip3 install virtualenv```

### Linux
1. Install MySQL
   * ```sudo apt-get update```
   * ```sudo apt-get install mysql-server```
   * ```sudo mysql_secure_installation```
2. Install virtualenv
   * ```pip3 install virtualenv```

### Windows
   TODO

## Setup
1. In the project repo, create a virtualenv pointing to your python3.
   ```virtualenv RestaurantListEnv --python=[path to python3]```
2. Activate the environment with ```source RestaurantListEnv/bin/activate```
3. Download the requirements with ```pip install -r Requirements.txt```
4. Run the database setup scripts ```./Scripts/setup-database.sh```
   * This script sets up a database with a test user for development.
5. Start the application with ```python3 wsgi.py```
6. Leave the virtural envrionment with ```deactivate```

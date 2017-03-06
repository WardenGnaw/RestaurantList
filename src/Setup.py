import sys
import pymysql
from flaskext.mysql import MySQL

def CreateRestaurantTable(cursor):
    cursor.execute("CREATE TABLE Restaurant (id INT AUTO_INCREMENT, name VARCHAR(100) NOT NULL, address VARCHAR(100) NOT NULL, PRIMARY KEY(id));")

def CreateFoodTable(cursor):
    cursor.execute("CREATE TABLE Food (id INT AUTO_INCREMENT, name VARCHAR(100), price DECIMAL(6,2), restaurant_id INT, PRIMARY KEY(id), FOREIGN KEY(restaurant_id) REFERENCES Restaurant(id));")

def CreateReviewTable(cursor):
    cursor.execute("CREATE TABLE Review (id INT AUTO_INCREMENT, text TEXT, rating TINYINT, food_id INT, PRIMARY KEY(id), FOREIGN KEY(food_id) REFERENCES Food(id));")

def SetupMySQL(app):
   mysql = MySQL()

   mysql_configuration = {}

   with open('.setup-files/mysql', 'r') as f:
      for lines in f:
         data = [item.strip() for item in lines.split('=')]
         mysql_configuration[data[0]] = data[1]

   # MySQL Configurations
   app.config['MYSQL_DATABASE_USER'] = mysql_configuration['USERNAME']
   app.config['MYSQL_DATABASE_PASSWORD'] = mysql_configuration['PASSWORD']
   app.config['MYSQL_DATABASE_DB'] = mysql_configuration['DATABASE']
   app.config['MYSQL_DATABASE_HOST'] = mysql_configuration["HOST"]

   mysql.init_app(app);

   try:
      conn = mysql.connect()
      cursor = conn.cursor()

      # Check to see if Restaurant table exists.
      cursor.execute("SHOW TABLES LIKE 'Restaurant';")
      if len(cursor.fetchall()) == 0:
         CreateRestaurantTable(cursor)

      # Check to see if Food table exists.
      cursor.execute("SHOW TABLES LIKE 'Food';")
      if len(cursor.fetchall()) == 0:
         CreateFoodTable(cursor)

      # Check to see if Review table exists.
      cursor.execute("SHOW TABLES LIKE 'Review';")
      if len(cursor.fetchall()) == 0:
         CreateReviewTable(cursor)

   except pymysql.err.InternalError as e:
      print("MySQL connection failed. Reason: {}".format(e))
      print("If database is unknown or not found. please run the script in 'Scripts/setup-test-database.sh'")
      sys.exit(1)

   return mysql;

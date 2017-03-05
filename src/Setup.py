from flaskext.mysql import MySQL

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

   return mysql;

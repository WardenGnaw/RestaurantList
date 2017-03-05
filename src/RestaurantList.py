from flask import Flask
from src.Setup import SetupMySQL

# Global Objects for Flask
app = Flask(__name__)
mysql = SetupMySQL(app)


@app.route("/")
def main():
   return "<h1 style='color:blue'>Hello</h1>"

@app.route("/andrew")
def andrew():
   conn = mysql.connect()
   cursor = conn.cursor()
   cursor.execute("SELECT * FROM Restaurant;")
   return str(cursor.fetchall())

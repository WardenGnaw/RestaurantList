from flask import Flask, render_template
from src.Setup import SetupMySQL

# Global Objects for Flask
app = Flask(__name__)
mysql = SetupMySQL(app)


@app.route("/")
def main():
   return render_template('index.html')

@app.route("/list")
def list_restaurants():
   conn = mysql.connect()
   cursor = conn.cursor()
   cursor.execute("SELECT * FROM Restaurant;")
   return render_template('restaurant_listing.html', restaurants=cursor.fetchall())

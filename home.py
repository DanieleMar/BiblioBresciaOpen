from flask import Flask, render_template, request
import json
from flask_bootstrap import Bootstrap
import datetime
import locale
import sqlite3 as sql



app = Flask(__name__)



def create_app():
  app = Flask(__name__)
  Bootstrap(app) 

  return app



@app.context_processor
def inject_today_date():

  locale.setlocale(locale.LC_TIME, 'it_IT.UTF-8') #traduce la data in italiano
  return {'today_date': datetime.date.today().strftime("%d %B %Y")} #mostra data




openjson = json.load(open("dati/open.json", "r")) 
chiusejson = json.load(open("dati/chiuse.json", "r"))


    
      

## USATO QUANDO HANNO CHIUSO LE BIBLIOTECHE PER LOCKDOWN
# @app.route("/")
# def load_page():
#   return render_template('sospeso.html') 


@app.route('/')
def list():
  try:
    con = sql.connect("manageDB\dbFiles\orari.db")
    con.row_factory = sql.Row
  
    cur = con.cursor()
    cur.execute("select * from aperte")
    open = cur.fetchall(); 

    cur.execute("select * from chiuse")
    close = cur.fetchall()

    return render_template("bbo-home.html", aperte = open, chiuse = close )
  except sql.Error as error:
    print("Fail: ", error)
  
  




if __name__ == '__main__':
 # app.run(debug=True)  #per debug
  app.run() 

  

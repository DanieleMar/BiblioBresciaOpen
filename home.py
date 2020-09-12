from flask import Flask, render_template, request
import json
from flask_bootstrap import Bootstrap
import datetime
import locale




app = Flask(__name__)



def create_app():
  app = Flask(__name__)
  Bootstrap(app) 

  return app



@app.context_processor
def inject_today_date():

  #TODO locale.setlocale(locale.LC_TIME, 'it_IT') #traduce la data in italiano
  return {'today_date': datetime.date.today().strftime("%d %B %Y")}




openjson=json.load(open("open.json", "r")) 
chiusejson=json.load(open("chiuse.json", "r"))


@app.route("/")

def load_page():
  try:
      return render_template('bbo-home.html', listaAperte=openjson["biblio"], listaChiuse=chiusejson["chiuse"]) 
  except KeyError as e:
    print("errore è: "+ str(e))
    if str(e)=="'biblio'":
      return render_template('bbo-home.html', listaAperte="", listaChiuse=chiusejson["chiuse"])
    return (str(e))
    
      

  



if __name__ == '__main__':
  #app.run(debug=True)  #per debug
  app.run() 

  

from flask import Flask, render_template, request
import json
from flask_bootstrap import Bootstrap
import datetime


app = Flask(__name__)



def create_app():
  app = Flask(__name__)
  Bootstrap(app)

  return app

@app.context_processor
def inject_today_date():

  return {'today_date': datetime.date.today().strftime("%d %B %Y")}




openjson=json.load(open("open.json", "r")) 
chiusejson=json.load(open("chiuse.json", "r"))

#@app.route("/")
@app.route("/bresciabibliopen")

def load_page():
  try:
      return render_template('bbo-home.html', listaAperte=openjson["biblio"], listaChiuse=chiusejson["chiuse"]) 
  except KeyError as e:
    print("errore è: "+ str(e))
    if str(e)=="'biblio'":
      return render_template('bbo-home.html', listaAperte="", listaChiuse=chiusejson["chiuse"])
    return (str(e))
    
      

  



if __name__ == '__main__':
  #app.run(debug=True, host='0.0.0.0') #per repl.it
  app.run(debug=True) #per il resto



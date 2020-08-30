from flask import Flask, render_template, request
import json
from flask_bootstrap import Bootstrap

#import per ricorrente
""" import time
import atexit
from apscheduler.schedulers.background import BackgroundScheduler
 """
app = Flask(__name__)

def create_app():
  app = Flask(__name__)
  Bootstrap(app)

  return app




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
  app.run(debug=True)



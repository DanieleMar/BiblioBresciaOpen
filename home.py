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


readjsonfile= open("open.json", "r") #apri file json

listajson=json.load(readjsonfile) #carica in variabile json
listaChiuseJson=json.load(open("chiuse.json", "r"))

@app.route("/")

def load_page():
    try:
      return render_template('bbo-home.html', listaAperte=listajson["biblio"], listaChiuse=listaChiuseJson["chiuse"]) 
    except Exception as err:
      print(err)


if __name__ == '__main__':
    app.run(debug=True)



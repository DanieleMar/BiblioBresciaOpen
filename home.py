from flask import Flask, render_template, request
import json
from flask_bootstrap import Bootstrap

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
    return render_template('bbo-home.html', listaAperte=listajson["biblio"], listaChiuse=listaChiuseJson["chiuse"]) 


# TEST PER IMPARARE I FLASK TEMPLATES #
lista1=["abaco", "lemure", "ciuberter"]
@app.route("/test")
def load_pg():
    name= "gianni"
    return render_template("test.html", nome=name, navigation=lista1) 

if __name__ == '__main__':
    app.run(debug=True)


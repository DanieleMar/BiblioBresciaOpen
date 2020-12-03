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

  locale.setlocale(locale.LC_TIME, 'it_IT.UTF-8') #traduce la data in italiano
  return {'today_date': datetime.date.today().strftime("%d %B %Y")} #mostra data




openjson = json.load(open("dati/open.json", "r")) 
chiusejson = json.load(open("dati/chiuse.json", "r"))

# FUNZIONA. MA CAMBIO PER FARE PAGINA TEMPORANEA
# @app.route("/")

# def load_page():
  # try:
  #     return render_template('bbo-home.html', listaAperte=openjson["biblio"], listaChiuse=chiusejson["chiuse"]) 
  # except KeyError as e:
  #   print("Errore: "+ str(e))
  #   if str(e)=="'biblio'": #se nessuna biblio è aperta, lascia la tabella vuota
  #     return render_template('bbo-home.html', listaAperte="", listaChiuse=chiusejson["chiuse"])
  #   return (str(e))
    
      

@app.route("/")
def load_page():
  return render_template('sospeso.html') 


if __name__ == '__main__':
  app.run(debug=True)  #per debug
 # app.run() 

  

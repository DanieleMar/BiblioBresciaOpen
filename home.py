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
    return render_template('bbo-home.html', listaAperte=listajson["biblio"], listaChiuse=listaChiuseJson["chiuse"]) 


# TEST PER IMPARARE I FLASK TEMPLATES #
lista1=["abaco", "lemure", "ciuberter"]
@app.route("/test")
def load_pg():
    name= "gianni"
    return render_template("test.html", nome=name, navigation=lista1) 

if __name__ == '__main__':
    app.run(debug=True)


#funzione per ricorrenza
""" 
def print_date_time():
    print(time.strftime("%A, %d. %B %Y %I:%M:%S %p"))


scheduler = BackgroundScheduler()
scheduler.add_job(func=print_date_time, trigger="interval", seconds=3)
scheduler.start()

# Shut down the scheduler when exiting the app
atexit.register(lambda: scheduler.shutdown()) """

#imposto cronjob - aggiorna ogni giorno file json
from datetime import datetime

def cronjob():
    """
    Main cron job.
    The main cronjob to be run continuously.
    """
    print("Cron job is running")
    print("Tick! The time is: %s" % datetime.now())
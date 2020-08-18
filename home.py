from flask import Flask, render_template, request
import json
from flask_bootstrap import Bootstrap
import boto3
from config import S3_BUCKET, S3_KEY, S3_SECRET


s3 = boto3.resource(
    's3',
    aws_access_key_id=S3_KEY,
    aws_secret_access_key=S3_SECRET
)



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


@app.route('/files')
def files():
    s3_resource = boto3.resource('s3')
    my_bucket = s3_resource.Bucket(S3_BUCKET)
    summaries = my_bucket.objects.all()

    return render_template('files.html', my_bucket=my_bucket, files=summaries)


if __name__ == '__main__':
    app.run(debug=True)



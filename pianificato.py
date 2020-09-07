from datetime import datetime 
from threading import Timer 
import scrapercitta 

x=datetime.today() 
print(x) 
#y=x.replace(day=x.day+1, hour=4, minute=30, second=0, microsecond=0) giusto, ogni giorno alle 3 

y=x.replace(day=x.day, hour=12, minute=15, second=0, microsecond=0) 
delta_t=y-x 
print(y) 
print(delta_t) 
secs=delta_t.seconds+1 
print(secs) 

def scraper(): 
    print ("hello world") 
    scrapercitta.run() #esegui file python test.py 

t = Timer(secs, scraper) 
t.start()

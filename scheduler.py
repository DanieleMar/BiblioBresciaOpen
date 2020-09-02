import schedule
import time
import scrapercitta
import threading

def job():
    print("I'm working...")
    scrapercitta.run()

schedule.every(30).seconds.do(job)
#schedule.every().minutes.do(job)
#schedule.every().hour.do(job)
#schedule.every().day.at("10:30").do(job)
print("log: scheduled -scrapingcitta.py ha fatto 1 giro")
#schedule.run_continuously()

while 1:
    schedule.run_pending()
    time.sleep(1)







#VERSIONE ALTERNATIVA CHE AVVIA UN THREAD IN BACKGROUND
# # while 1:
# #     schedule.run_pending()
# #     time.sleep(1)

# class ScheduleThread(threading.Thread): #avvia thread per scheduler in background. 
#     def __init__(self, *pargs, **kwargs):
#         super().__init__(*pargs, daemon=True, name="scheduler", **kwargs)

#     def run(self):
        
#         schedule.every().seconds.do(job)
#         schedule.every().minutes.do(job)
#         schedule.every().hour.do(job)
#         schedule.every().day.at("10:30").do(job)
        
#         while True:
#             schedule.run_pending()
#             time.sleep(schedule.idle_seconds())

# ScheduleThread().start()
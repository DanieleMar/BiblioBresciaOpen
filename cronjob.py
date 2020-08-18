# Package Scheduler.
from apscheduler.schedulers.blocking import BlockingScheduler

# Main cronjob function.
import scrapercitta

# Create an instance of scheduler and add function.
scheduler = BlockingScheduler()
scheduler.add_job(scrapercitta, "interval", hours=20)

scheduler.start()
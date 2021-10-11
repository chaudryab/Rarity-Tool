from apscheduler.schedulers.background import BackgroundScheduler
from .views import get_data_excel

#------------- Get Data From Excel --------------
def start():
    scheduler = BackgroundScheduler()
    scheduler.add_job(get_data_excel, 'interval', seconds=86400)
    scheduler.start()
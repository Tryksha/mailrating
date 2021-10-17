from celery import Celery
import datetime
from django.core.mail import send_mail
from django.conf import settings


app = Celery('send_mail', broker='redis://localhost')



@app.task
def s_mail():
    time_threshold = datetime.now() - datetime.timedelta(hours = 2)
    subject = 'auto mail'
    message = 'auto mail'
    email_from = 'pk6222307@gmail.com'
    recipient_list = ['paliwalap7@gmail.com']
    send_mail(subject, message, email_from, recipient_list)
import os
from django.conf import settings
from celery import Celery
from celery.schedules import crontab
from django.core.mail import send_mail

# Set the default Django settings module for the 'celery' program.
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'mailrating.settings')

app = Celery('mailrating')

# Using a string here means the worker doesn't have to serialize
# the configuration object to child processes.
# - namespace='CELERY' means all celery-related configuration keys
#   should have a `CELERY_` prefix.
app.config_from_object('django.conf:settings', namespace='CELERY')

# Load task modules from all registered Django apps.
app.autodiscover_tasks()

@app.task(bind = True)
def debug_task(self):
    print('Hello form celery')

@app.task
def print_hello():
    print("hello from function")

@app.task
def mail_sender():
    # import datetime
    from django.core.mail import send_mail
    from django.conf import settings
    subject = 'auto mail'
    message = 'auto mail'
    email_from = 'pk6222307@gmail.com'
    recipient_list = ['paliwalap7@gmail.com']
    send_mail(subject, message, email_from, recipient_list)

# app.autodiscover_tasks(lambda:settings.INSTALLED_APPS)

# app.conf.beat_schedule = {
#     'add-every-2-hour':{
#         'task':'s_mail',
#         'schedule':crontab(minute='*/1')
#     }
# }

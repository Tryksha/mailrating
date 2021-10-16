
from django.core.mail import send_mail


def my_scheduled_job():
  send_mail(
    'Subject here',
    'Here is the message.',
    ['paliwalap7@gmail.com'],
    fail_silently=False,
)
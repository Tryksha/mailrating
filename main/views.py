from django.shortcuts import render, HttpResponse
from django.core.mail import send_mail
# Create your views here.

def home(request):
    subject = 'auto mail'
    message = 'auto mail'
    email_from = 'pk6222307@gmail.com'
    recipient_list = ['paliwalap7@gmail.com']
    send_mail(subject, message, email_from, recipient_list)
    return HttpResponse('mail sent sucessfully')
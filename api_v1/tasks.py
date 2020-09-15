from celery import shared_task
from django.core.mail import send_mail

from time import sleep

@shared_task
def sleepy(duration):
    sleep(duration)
    return None

@shared_task
def send_email_task():
    send_mail('Celery task worked!', 'This is proof that worked!', 'seyit@gmail.com', ['seyitbu1111@gmail.com'])

    return None
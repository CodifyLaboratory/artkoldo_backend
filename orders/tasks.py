from celery import shared_task
from django.core.mail import send_mail


@shared_task
def send_message_to_customer(**kwargs):
    send_mail(**kwargs)

from django.db.models.signals import post_save
from django.dispatch import receiver
from django.conf import settings
from .models import Order
from .tasks import send_message_to_customer


@receiver(post_save, sender=Order)
def order_create(sender, instance, created, **kwargs):
    if created:
        subject = 'Имеется заказ. ПИСЬМО НЕ ПЕРЕСЫЛАТЬ!!!'
        message = f'заказанно на сумму {instance.total_price} заказчик - {instance.name}'
        from_email = settings.EMAIL_HOST_USER
        to_list = [instance.email]
        send_message_to_customer.delay(
            subject=subject, message=message, from_email=from_email, recipient_list=to_list, fail_silently=False
        )

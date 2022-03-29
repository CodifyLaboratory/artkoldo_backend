from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import Order
from django.conf import settings
from django.urls import reverse
from django.core.mail import send_mail


@receiver(post_save, sender=Order)
def order_created(instance, created, **kwargs):
    if created:
        link = ", ".join([
            "http://127.0.0.1:8000{}".format(
                reverse('admin:{}_{}_change'.format('orders', 'order'),
                        args=(instance.id,)),
            )
        ])
        message = f"Номер заказа: {instance.id} \n" \
                  f"Имя: {instance.name} \n" \
                  f"Ссылка на заказ в админ панели: {link}"
        send_mail(
            subject=f"Заказ №{instance.id}",
            message=message,
            from_email=settings.EMAIL_HOST_USER,
            # можно написать один или несколько адресов электронной почты. надо написать через запятую
            recipient_list=["artkoldoo2022@gmail.com", 'chenye797@gmail.com']
        )

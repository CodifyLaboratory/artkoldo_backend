from django.db import models
from products.models import Painting, Handicraft, Ceramic


class PaintingOrder(models.Model):
    customer_name = models.CharField(max_length=100, verbose_name='Имя заказчика')
    phone_number = models.CharField(max_length=14, verbose_name='Номер телефона заказчика')
    product = models.ForeignKey(Painting, on_delete=models.CASCADE, blank=True, null=True, verbose_name='Заказанная картина')
    quantity = models.PositiveIntegerField(blank=True, null=True, verbose_name='Количество')
    price = models.PositiveIntegerField(blank=True, null=True, verbose_name='Цена за единицу')
    total_sum = models.PositiveIntegerField(blank=True, null=True, verbose_name=' Общая сумма')
    order_status = models.BooleanField(default=False, verbose_name='Статус заказа')
    created = models.DateTimeField(auto_now=True, verbose_name='Дата заказа')

    class Meta:
        verbose_name = 'Заказ картины'
        verbose_name_plural = "Заказ картин"
        ordering = ['-created']

    def __str__(self):
        return f'{self.customer_name} {self.product}'


class HandicraftOrder(models.Model):
    customer_name = models.CharField(max_length=100, verbose_name='Имя заказчика')
    phone_number = models.CharField(max_length=14, verbose_name='Номер телефона заказчика')
    product = models.ForeignKey(Handicraft, on_delete=models.CASCADE, blank=True, null=True, verbose_name='Заказанное ремесленное изделие')
    quantity = models.PositiveIntegerField(blank=True, null=True, verbose_name='Количество')
    price = models.PositiveIntegerField(blank=True, null=True, verbose_name='Цена за единицу')
    total_sum = models.PositiveIntegerField(blank=True, null=True, verbose_name=' Общая сумма')
    order_status = models.BooleanField(default=False, verbose_name='Статус заказа')
    created = models.DateTimeField(auto_now=True, verbose_name='Дата заказа')

    class Meta:
        verbose_name = 'Заказ ремесленного изделия'
        verbose_name_plural = "Заказ ремесленных изделий"
        ordering = ['-created']

    def __str__(self):
        return f'{self.customer_name} {self.product}'


class CeramicOrder(models.Model):
    customer_name = models.CharField(max_length=100, verbose_name='Имя заказчика')
    phone_number = models.CharField(max_length=14, verbose_name='Номер телефона заказчика')
    product = models.ForeignKey(Ceramic, on_delete=models.CASCADE, blank=True, null=True, verbose_name='Заказанное керамическое изделие')
    quantity = models.PositiveIntegerField(blank=True, null=True, verbose_name='Количество')
    price = models.PositiveIntegerField(blank=True, null=True, verbose_name='Цена за единицу')
    total_sum = models.PositiveIntegerField(blank=True, null=True, verbose_name=' Общая сумма')
    order_status = models.BooleanField(default=False, verbose_name='Статус заказа')
    created = models.DateTimeField(auto_now=True, verbose_name='Дата заказа')

    class Meta:
        verbose_name = 'Заказ керамического изделия'
        verbose_name_plural = "Заказ керамических изделий"
        ordering = ['-created']

    def __str__(self):
        return f'{self.customer_name} {self.product}'

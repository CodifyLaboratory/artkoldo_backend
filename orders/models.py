from django.db import models
from products.models import Painting, Handicraft, Ceramic


class PaintingOrder(models.Model):
    customer_name = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=14)
    product = models.ForeignKey(Painting, on_delete=models.CASCADE, blank=True, null=True)
    quantity = models.PositiveIntegerField(blank=True, null=True)
    price = models.PositiveIntegerField(blank=True, null=True)
    total_sum = models.PositiveIntegerField(blank=True, null=True)
    order_status = models.BooleanField(default=False)

    def __str__(self):
        return f'{self.customer_name} {self.product}'


class HandicraftOrder(models.Model):
    customer_name = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=14)
    product = models.ForeignKey(Handicraft, on_delete=models.CASCADE, blank=True, null=True)
    quantity = models.PositiveIntegerField(blank=True, null=True)
    price = models.PositiveIntegerField(blank=True, null=True)
    total_sum = models.PositiveIntegerField(blank=True, null=True)
    order_status = models.BooleanField(default=False)

    def __str__(self):
        return f'{self.customer_name} {self.product}'


class CeramicOrder(models.Model):
    customer_name = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=14)
    product = models.ForeignKey(Ceramic, on_delete=models.CASCADE, blank=True, null=True)
    quantity = models.PositiveIntegerField(blank=True, null=True)
    price = models.PositiveIntegerField(blank=True, null=True)
    total_sum = models.PositiveIntegerField(blank=True, null=True)
    order_status = models.BooleanField(default=False)

    def __str__(self):
        return f'{self.customer_name} {self.product}'

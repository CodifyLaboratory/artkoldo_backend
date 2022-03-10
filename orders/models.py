from django.db import models


class OrderStatus(models.Model):
    title = models.CharField(max_length=250, verbose_name='Статус заказа')

    class Meta:
        verbose_name = 'Статус заказа'
        verbose_name_plural = "Статусы заказа"
        ordering = ['title']

    def __str__(self):
        return self.title


class Order(models.Model):
    name = models.CharField(max_length=100, verbose_name='Имя заказчика')
    email = models.EmailField(verbose_name='Почта')
    phone = models.CharField(max_length=100, verbose_name='Номер телефона')
    country = models.CharField(max_length=250, verbose_name='Страна доставки')
    region = models.CharField(max_length=250, verbose_name='Область')
    city = models.CharField(max_length=250, verbose_name='Город/Населенный пункт')
    comment = models.CharField(max_length=255, verbose_name='Комментарии к заказу')
    created_date = models.DateTimeField(verbose_name='Дата создания заказа', auto_now_add=True)
    total_price = models.FloatField(verbose_name='Итоговая стоимость заказа')
    order_status = models.ForeignKey(OrderStatus, on_delete=models.CASCADE, verbose_name='Статус Заказа', default=1)
    quantity = models.PositiveIntegerField(verbose_name='Количество')
    price = models.PositiveIntegerField(verbose_name='Цена за единицу')
    products_id = models.PositiveIntegerField(verbose_name='Артикул товара')
    product_name = models.CharField(max_length=255, verbose_name='Наименование товара')

    class Meta:
        verbose_name = 'Заказ'
        verbose_name_plural = "Заказы"
        ordering = ['created_date']

    def __str__(self):
        return f' Имя заказчика: {self.name} | статус заказа: {self.order_status}'

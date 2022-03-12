from django.db import models


class Founder(models.Model):
    description = models.TextField(verbose_name='Об основателе', blank=True, null=True)
    photo = models.ImageField(upload_to='founder_photo', blank=True, null=True)


class AboutUs(models.Model):
    description = models.TextField(verbose_name='О компании', blank=True, null=True)


class Contacts(models.Model):
    phone_number_1 = models.CharField(max_length=13, verbose_name='Номер телефона 1', blank=True, null=True)
    phone_number_2 = models.CharField(max_length=13, verbose_name='Номер телефона 2', blank=True, null=True)
    phone_number_3 = models.CharField(max_length=13, verbose_name='Номер телефона 3', blank=True, null=True)
    address = models.CharField(max_length=255, verbose_name='Адрес компании', blank=True, null=True)
    email = models.EmailField(verbose_name='Емейл адрес', blank=True, null=True)


class SocialMedia(models.Model):
    instagram_link = models.URLField(verbose_name='Ссылка на инстаграм', blank=True, null=True)
    facebook_link = models.URLField(verbose_name='Ссылка на фейсбук', blank=True, null=True)
    telegram_link = models.URLField(verbose_name='Сссылка на телеграм', blank=True, null=True)
    whatsapp_link = models.URLField(verbose_name='Ссылка на Whatsapp', blank=True, null=True)


class ContactForm(models.Model):
    description = models.TextField(verbose_name='Описание', blank=True, null=True)
    name = models.CharField(max_length=100, verbose_name='Имя', blank=True, null=True)
    email = models.EmailField(verbose_name='Емейл', blank=True, null=True)
    phone_number = models.CharField(max_length=14, verbose_name='Номер телефона', blank=True, null=True)
    comment = models.TextField(verbose_name='Комментарий', blank=True, null=True)


class Terms(models.Model):
    conditions = models.TextField(verbose_name='Положения и условия', blank=True, null=True)
    privacy = models.TextField(verbose_name='Политика конфеденциальности', blank=True, null=True)
    copyright = models.TextField(verbose_name='Политика авторского права', blank=True, null=True)


class ForPartners(models.Model):
    description = models.TextField(verbose_name='Для партнёров', blank=True, null=True)


class PaymentDelivery(models.Model):
    payment = models.TextField(verbose_name='Оплата', blank=True, null=True)
    delivery = models.TextField(verbose_name='Доставка', blank=True, null=True)

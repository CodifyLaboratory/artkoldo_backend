from django.db import models


class Founder(models.Model):
    description = models.TextField(verbose_name='Об основателе', blank=True, null=True)
    photo = models.ImageField(upload_to='Фото', blank=True, null=True)

    class Meta:
        verbose_name = 'Основатели'
        verbose_name_plural = 'Основатели'


class AboutUs(models.Model):
    description = models.TextField(verbose_name='О компании', blank=True, null=True)
    founder = models.ManyToManyField(Founder, verbose_name='Основатели', blank=True)

    class Meta:
        verbose_name = 'О компании'
        verbose_name_plural = 'О компании'


class Contacts(models.Model):
    phone_number_1 = models.CharField(max_length=13, verbose_name='Номер телефона 1', blank=True, null=True)
    phone_number_2 = models.CharField(max_length=13, verbose_name='Номер телефона 2', blank=True, null=True)
    phone_number_3 = models.CharField(max_length=13, verbose_name='Номер телефона 3', blank=True, null=True)
    address = models.CharField(max_length=255, verbose_name='Адрес компании', blank=True, null=True)
    email = models.EmailField(verbose_name='Почта', blank=True, null=True)

    class Meta:
        verbose_name = 'Контакты'
        verbose_name_plural = 'Контакты'


class SocialMedia(models.Model):
    instagram_link = models.URLField(verbose_name='Ссылка на инстаграм', blank=True, null=True)
    facebook_link = models.URLField(verbose_name='Ссылка на фейсбук', blank=True, null=True)
    telegram_link = models.URLField(verbose_name='Ссылка на телеграм', blank=True, null=True)
    whatsapp_link = models.URLField(verbose_name='Ссылка на Whatsapp', blank=True, null=True)

    class Meta:
        verbose_name = 'Соц сети'
        verbose_name_plural = 'Соц сети'


class ContactForm(models.Model):
    name = models.CharField(max_length=100, verbose_name='Имя', blank=True, null=True)
    email = models.EmailField(verbose_name='Почта', blank=True, null=True)
    phone_number = models.CharField(max_length=14, verbose_name='Номер телефона', blank=True, null=True)
    comment = models.TextField(verbose_name='Комментарий', blank=True, null=True)


class Terms(models.Model):
    conditions = models.TextField(verbose_name='Положения и условия', blank=True, null=True)
    privacy = models.TextField(verbose_name='Политика конфеденциальности', blank=True, null=True)
    copyright = models.TextField(verbose_name='Политика авторского права', blank=True, null=True)

    class Meta:
        verbose_name = 'Положения и условия'
        verbose_name_plural = 'Положения и условия'


class ForPartners(models.Model):
    description = models.TextField(verbose_name='Для партнёров', blank=True, null=True)

    class Meta:
        verbose_name = 'Партнерам'
        verbose_name_plural = 'Партнерам'


class PaymentDelivery(models.Model):
    payment = models.TextField(verbose_name='Оплата', blank=True, null=True)
    delivery = models.TextField(verbose_name='Доставка', blank=True, null=True)

    class Meta:
        verbose_name = 'Оплата и доставка'
        verbose_name_plural = 'Оплата и доставка'

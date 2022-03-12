# Generated by Django 4.0.2 on 2022-03-12 10:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0010_painting_created_at_painting_discount_price_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='ceramic',
            name='created_at',
            field=models.DateTimeField(auto_now=True, null=True, verbose_name='Дата создания'),
        ),
        migrations.AddField(
            model_name='ceramic',
            name='discount_price',
            field=models.PositiveIntegerField(blank=True, null=True, verbose_name='Цена со скидкой'),
        ),
        migrations.AddField(
            model_name='ceramic',
            name='recommended',
            field=models.BooleanField(blank=True, default=False, null=True, verbose_name='Рекомендованный'),
        ),
        migrations.AddField(
            model_name='handicraft',
            name='created_at',
            field=models.DateTimeField(auto_now=True, null=True, verbose_name='Дата создания'),
        ),
        migrations.AddField(
            model_name='handicraft',
            name='discount_price',
            field=models.PositiveIntegerField(blank=True, null=True, verbose_name='Цена со скидкой'),
        ),
        migrations.AddField(
            model_name='handicraft',
            name='recommended',
            field=models.BooleanField(blank=True, default=False, null=True, verbose_name='Рекомендованный'),
        ),
    ]

# Generated by Django 4.0.2 on 2022-03-10 15:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0003_alter_order_options'),
    ]

    operations = [
        migrations.AlterField(
            model_name='orderstatus',
            name='title',
            field=models.CharField(max_length=250, unique=True, verbose_name='Статус заказа'),
        ),
    ]

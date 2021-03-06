# Generated by Django 4.0.2 on 2022-03-14 10:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('info', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='contactform',
            name='description',
        ),
        migrations.AlterField(
            model_name='contactform',
            name='email',
            field=models.EmailField(blank=True, max_length=254, null=True, verbose_name='Почта'),
        ),
        migrations.AlterField(
            model_name='contacts',
            name='email',
            field=models.EmailField(blank=True, max_length=254, null=True, verbose_name='Почта'),
        ),
        migrations.AlterField(
            model_name='founder',
            name='photo',
            field=models.ImageField(blank=True, null=True, upload_to='Фото'),
        ),
        migrations.AlterField(
            model_name='socialmedia',
            name='telegram_link',
            field=models.URLField(blank=True, null=True, verbose_name='Ссылка на телеграм'),
        ),
    ]

# Generated by Django 4.0.2 on 2022-03-12 10:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0008_alter_region_title_alter_author_unique_together_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='author',
            name='created_at',
            field=models.DateTimeField(auto_now=True, null=True, verbose_name='Дата создания'),
        ),
    ]
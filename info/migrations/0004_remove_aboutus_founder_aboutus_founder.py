# Generated by Django 4.0.2 on 2022-03-14 10:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('info', '0003_alter_aboutus_options_alter_contacts_options_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='aboutus',
            name='founder',
        ),
        migrations.AddField(
            model_name='aboutus',
            name='founder',
            field=models.ManyToManyField(blank=True, to='info.Founder', verbose_name='Основатели'),
        ),
    ]
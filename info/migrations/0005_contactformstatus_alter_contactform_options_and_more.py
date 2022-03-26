# Generated by Django 4.0.2 on 2022-03-26 09:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('info', '0004_remove_aboutus_founder_aboutus_founder'),
    ]

    operations = [
        migrations.CreateModel(
            name='ContactFormStatus',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=250, unique=True, verbose_name='Статус обратной связи')),
            ],
            options={
                'verbose_name': 'Статус обратной связи',
                'verbose_name_plural': 'Статус обратной связи',
                'ordering': ['title'],
            },
        ),
        migrations.AlterModelOptions(
            name='contactform',
            options={'verbose_name': 'Обратная связь', 'verbose_name_plural': 'Обратная связь'},
        ),
        migrations.AddField(
            model_name='contactform',
            name='created_at',
            field=models.DateTimeField(auto_now=True, verbose_name='Дата создания'),
        ),
        migrations.AlterField(
            model_name='contactform',
            name='comment',
            field=models.TextField(null=True, verbose_name='Комментарий'),
        ),
        migrations.AlterField(
            model_name='contactform',
            name='email',
            field=models.EmailField(max_length=254, null=True, verbose_name='Почта'),
        ),
        migrations.AlterField(
            model_name='contactform',
            name='name',
            field=models.CharField(max_length=100, null=True, verbose_name='Имя'),
        ),
        migrations.AlterField(
            model_name='contactform',
            name='phone_number',
            field=models.CharField(max_length=14, null=True, verbose_name='Номер телефона'),
        ),
        migrations.AddField(
            model_name='contactform',
            name='status',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='info.contactformstatus', verbose_name='Статус обратной связи'),
        ),
    ]

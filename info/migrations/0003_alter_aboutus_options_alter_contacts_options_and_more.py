# Generated by Django 4.0.2 on 2022-03-14 10:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('info', '0002_remove_contactform_description_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='aboutus',
            options={'verbose_name': 'О компании', 'verbose_name_plural': 'О компании'},
        ),
        migrations.AlterModelOptions(
            name='contacts',
            options={'verbose_name': 'Контакты', 'verbose_name_plural': 'Контакты'},
        ),
        migrations.AlterModelOptions(
            name='forpartners',
            options={'verbose_name': 'Партнерам', 'verbose_name_plural': 'Партнерам'},
        ),
        migrations.AlterModelOptions(
            name='founder',
            options={'verbose_name': 'Основатели', 'verbose_name_plural': 'Основатели'},
        ),
        migrations.AlterModelOptions(
            name='paymentdelivery',
            options={'verbose_name': 'Оплата и доставка', 'verbose_name_plural': 'Оплата и доставка'},
        ),
        migrations.AlterModelOptions(
            name='socialmedia',
            options={'verbose_name': 'Соц сети', 'verbose_name_plural': 'Соц сети'},
        ),
        migrations.AlterModelOptions(
            name='terms',
            options={'verbose_name': 'Положения и условия', 'verbose_name_plural': 'Положения и условия'},
        ),
        migrations.AddField(
            model_name='aboutus',
            name='founder',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='info.founder'),
        ),
    ]

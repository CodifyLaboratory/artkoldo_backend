# Generated by Django 4.0.2 on 2022-02-17 10:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0004_alter_country_title_alter_region_title'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='region',
            options={'ordering': ['title'], 'verbose_name': 'Регион', 'verbose_name_plural': 'Регионы'},
        ),
        migrations.RemoveField(
            model_name='author',
            name='origin',
        ),
        migrations.AddField(
            model_name='author',
            name='region',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='products.region', verbose_name='Регион'),
        ),
        migrations.AddField(
            model_name='region',
            name='country',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='products.country', verbose_name='Страна'),
        ),
        migrations.DeleteModel(
            name='Origin',
        ),
    ]
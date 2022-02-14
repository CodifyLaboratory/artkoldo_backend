# Generated by Django 4.0.2 on 2022-02-13 19:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='ceramicmaterial',
            options={'ordering': ['title'], 'verbose_name': 'Материал керамического изделия', 'verbose_name_plural': 'Материалы керамических изделий'},
        ),
        migrations.AlterModelOptions(
            name='ceramictechnique',
            options={'ordering': ['title'], 'verbose_name': 'Техника создания керамики', 'verbose_name_plural': 'Техники создания керамики'},
        ),
        migrations.AlterModelOptions(
            name='ceramictype',
            options={'ordering': ['title'], 'verbose_name': 'Тип керамики', 'verbose_name_plural': 'Типы керамики'},
        ),
        migrations.AlterModelOptions(
            name='handicraftmaterial',
            options={'ordering': ['title'], 'verbose_name': 'Материал ремесленного изделия', 'verbose_name_plural': 'Материалы ремесленных изделий'},
        ),
        migrations.AlterModelOptions(
            name='handicrafttechnique',
            options={'ordering': ['title'], 'verbose_name': 'Техника ремесла', 'verbose_name_plural': 'Техники ремесла'},
        ),
        migrations.AlterModelOptions(
            name='handicrafttype',
            options={'ordering': ['title'], 'verbose_name': 'Тип ремесленного изделия', 'verbose_name_plural': 'Типы ремесленных изделий'},
        ),
        migrations.AlterModelOptions(
            name='paintmaterial',
            options={'ordering': ['title'], 'verbose_name': 'Материал живописи', 'verbose_name_plural': 'Материалы живописи'},
        ),
        migrations.AlterModelOptions(
            name='painttechnique',
            options={'ordering': ['title'], 'verbose_name': 'Техника живописи', 'verbose_name_plural': 'Техники живописи'},
        ),
        migrations.AlterModelOptions(
            name='style',
            options={'ordering': ['title'], 'verbose_name': 'Стиль живописи', 'verbose_name_plural': 'Стили живописи'},
        ),
        migrations.AlterModelOptions(
            name='subject',
            options={'ordering': ['title'], 'verbose_name': 'Тема картины', 'verbose_name_plural': 'Темы картины'},
        ),
        migrations.AddField(
            model_name='ceramic',
            name='description',
            field=models.TextField(blank=True, max_length=500, null=True, verbose_name='Описание'),
        ),
        migrations.AddField(
            model_name='ceramic',
            name='keywords',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='Ключевые слова'),
        ),
        migrations.AddField(
            model_name='handicraft',
            name='description',
            field=models.TextField(blank=True, max_length=500, null=True, verbose_name='Описание'),
        ),
        migrations.AddField(
            model_name='handicraft',
            name='keywords',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='Ключевые слова'),
        ),
        migrations.AddField(
            model_name='painting',
            name='description',
            field=models.TextField(blank=True, max_length=500, null=True, verbose_name='Описание'),
        ),
        migrations.AddField(
            model_name='painting',
            name='keywords',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='Ключевые слова'),
        ),
        migrations.AlterField(
            model_name='ceramicmaterial',
            name='title',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='Материал керамического изделия'),
        ),
        migrations.AlterField(
            model_name='ceramictype',
            name='title',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='Тип керамики'),
        ),
        migrations.AlterField(
            model_name='handicraftmaterial',
            name='title',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='Материал ремесленного изделия'),
        ),
        migrations.AlterField(
            model_name='handicrafttype',
            name='title',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='Тип ремесленного изделия'),
        ),
    ]

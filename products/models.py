from django.db import models


'''
    Universal attributes
'''
class Origin(models.Model):
    country = models.CharField(max_length=100, verbose_name='Страна', null=True, blank=True)
    region = models.CharField(max_length=100, verbose_name='Область', null=True, blank=True)

    class Meta:
        verbose_name = 'Регион'
        verbose_name_plural = "Регионы"
        ordering = ['country']

    def __str__(self):
        return f'{self.country}, {self.region}'


class Author(models.Model):
    name = models.CharField(max_length=255, verbose_name='Ф.И. автора', null=True, blank=True)
    phone_number = models.CharField(max_length=13, verbose_name='Номер телефона', null=True, blank=True)
    about = models.TextField(verbose_name='Об авторе', null=True, blank=True)
    origin = models.ForeignKey(Origin, on_delete=models.PROTECT, verbose_name='Регион', null=True, blank=True)

    class Meta:
        verbose_name = 'Автора'
        verbose_name_plural = "Авторы"
        ordering = ['name']

    def __str__(self):
        return self.name


class Color(models.Model):
    title = models.CharField(max_length=100, verbose_name='Цвет', null=True, blank=True)
    code = models.CharField(max_length=7, verbose_name='Код цвета', null=True, blank=True)

    class Meta:
        verbose_name = 'Цвет'
        verbose_name_plural = "Цвета"
        ordering = ['title']

    def __str__(self):
        return self.title


'''
    Paintings
'''
class Subject(models.Model):
    title = models.CharField(max_length=100, verbose_name='Тема картины', null=True, blank=True)

    class Meta:
        verbose_name = 'Тема картины'
        verbose_name_plural = "Темы картины"
        ordering = ['title']

    def __str__(self):
        return self.title


class PaintMaterial(models.Model):
    title = models.CharField(max_length=100, verbose_name='Материал живописи', null=True, blank=True)

    class Meta:
        verbose_name = 'Материал живописи'
        verbose_name_plural = "Материалы живописи"
        ordering = ['title']

    def __str__(self):
        return self.title


class Style(models.Model):
    title = models.CharField(max_length=100, verbose_name='Стиль живописи', null=True, blank=True)

    class Meta:
        verbose_name = 'Стиль живописи'
        verbose_name_plural = "Стили живописи"
        ordering = ['title']

    def __str__(self):
        return self.title


class PaintTechnique(models.Model):
    title = models.CharField(max_length=100, verbose_name='Техника живописи', null=True, blank=True)

    class Meta:
        verbose_name = 'Техника живописи'
        verbose_name_plural = "Техники живописи"
        ordering = ['title']

    def __str__(self):
        return self.title


class Painting(models.Model):
    category = 'Paintings'
    title = models.CharField(max_length=100, verbose_name='Название картины', null=True, blank=True)
    photo = models.ImageField(verbose_name='Фото', upload_to='paintings_images', null=True, blank=True)
    description = models.TextField(max_length=500, verbose_name='Описание', null=True, blank=True)
    subject = models.ForeignKey(Subject, on_delete=models.SET_NULL, verbose_name='Тема', null=True, blank=True)
    material = models.ForeignKey(PaintMaterial, on_delete=models.SET_NULL, verbose_name='Материал', null=True, blank=True)
    style = models.ForeignKey(Style, on_delete=models.SET_NULL, verbose_name='Стиль', null=True, blank=True)
    technique = models.ForeignKey(PaintTechnique, on_delete=models.SET_NULL, verbose_name='Техника', null=True, blank=True)
    color = models.ManyToManyField(Color, verbose_name='Цвет', blank=True)
    width = models.PositiveIntegerField(verbose_name='Ширина (см)', null=True, blank=True)
    height = models.PositiveIntegerField(verbose_name='Высота (см)', null=True, blank=True)
    author = models.ForeignKey(Author, on_delete=models.SET_NULL, verbose_name='Автор', null=True, blank=True)
    price = models.PositiveIntegerField(verbose_name='Цена', null=True, blank=True)
    keywords = models.CharField(max_length=100, verbose_name='Ключевые слова', null=True, blank=True)

    class Meta:
        verbose_name = 'Картина'
        verbose_name_plural = 'Картины'
        ordering = ['title']

    def __str__(self):
        return f'{self.title}, {self.author}'


'''
    Handicrafts
'''
class HandicraftType(models.Model):
    title = models.CharField(max_length=100, verbose_name='Тип ремесленного изделия', null=True, blank=True)

    class Meta:
        verbose_name = 'Тип ремесленного изделия'
        verbose_name_plural = "Типы ремесленных изделий"
        ordering = ['title']

    def __str__(self):
        return self.title


class HandicraftMaterial(models.Model):
    title = models.CharField(max_length=100, verbose_name='Материал ремесленного изделия', null=True, blank=True)

    class Meta:
        verbose_name = 'Материал ремесленного изделия'
        verbose_name_plural = "Материалы ремесленных изделий"
        ordering = ['title']

    def __str__(self):
        return self.title


class HandicraftTechnique(models.Model):
    title = models.CharField(max_length=100, verbose_name='Техника создания', null=True, blank=True)

    class Meta:
        verbose_name = 'Техника ремесла'
        verbose_name_plural = "Техники ремесла"
        ordering = ['title']

    def __str__(self):
        return self.title


class Handicraft(models.Model):
    category = 'Handicrafts'
    title = models.CharField(max_length=100, verbose_name='Название изделия', null=True, blank=True)
    photo = models.ImageField(verbose_name='Фото', upload_to='handicrafts_images', null=True, blank=True)
    description = models.TextField(max_length=500, verbose_name='Описание', null=True, blank=True)
    type = models.ForeignKey(HandicraftType, on_delete=models.SET_NULL, verbose_name='Тип изделия', null=True, blank=True)
    material = models.ForeignKey(HandicraftMaterial, on_delete=models.SET_NULL, verbose_name='Материал', null=True, blank=True)
    technique = models.ForeignKey(HandicraftTechnique, on_delete=models.SET_NULL, verbose_name='Техника', null=True, blank=True)
    color = models.ManyToManyField(Color, verbose_name='Цвет', blank=True)
    author = models.ForeignKey(Author, on_delete=models.SET_NULL, verbose_name='Автор', null=True, blank=True)
    price = models.PositiveIntegerField(verbose_name='Цена', null=True, blank=True)
    keywords = models.CharField(max_length=100, verbose_name='Ключевые слова', null=True, blank=True)

    class Meta:
        verbose_name = 'Ремесленное изделие'
        verbose_name_plural = 'Ремесленные изделия'
        ordering = ['title']

    def __str__(self):
        return f'{self.title}, {self.author}'


'''
    Ceramics
'''
class CeramicType(models.Model):
    title = models.CharField(max_length=100, verbose_name='Тип керамики', null=True, blank=True)

    class Meta:
        verbose_name = 'Тип керамики'
        verbose_name_plural = "Типы керамики"
        ordering = ['title']

    def __str__(self):
        return self.title


class CeramicMaterial(models.Model):
    title = models.CharField(max_length=100, verbose_name='Материал керамического изделия', null=True, blank=True)

    class Meta:
        verbose_name = 'Материал керамического изделия'
        verbose_name_plural = "Материалы керамических изделий"
        ordering = ['title']

    def __str__(self):
        return self.title


class CeramicTechnique(models.Model):
    title = models.CharField(max_length=100, verbose_name='Техника создания', null=True, blank=True)

    class Meta:
        verbose_name = 'Техника создания керамики'
        verbose_name_plural = "Техники создания керамики"
        ordering = ['title']

    def __str__(self):
        return self.title


class Ceramic(models.Model):
    category = 'Ceramics'
    title = models.CharField(max_length=100, verbose_name='Название изделия', null=True, blank=True)
    photo = models.ImageField(verbose_name='Фото', upload_to='ceramics_images', null=True, blank=True)
    description = models.TextField(max_length=500, verbose_name='Описание', null=True, blank=True)
    type = models.ForeignKey(CeramicType, on_delete=models.SET_NULL, verbose_name='Тип изделия', null=True, blank=True)
    material = models.ForeignKey(CeramicMaterial, on_delete=models.SET_NULL, verbose_name='Материал', null=True, blank=True)
    technique = models.ForeignKey(CeramicTechnique, on_delete=models.SET_NULL, verbose_name='Техника', null=True, blank=True)
    color = models.ManyToManyField(Color, verbose_name='Цвет', blank=True)
    author = models.ForeignKey(Author, on_delete=models.SET_NULL, verbose_name='Автор', null=True, blank=True)
    price = models.PositiveIntegerField(verbose_name='Цена', null=True, blank=True)
    keywords = models.CharField(max_length=100, verbose_name='Ключевые слова', null=True, blank=True)

    class Meta:
        verbose_name = 'Керамика'
        verbose_name_plural = 'Керамика'
        ordering = ['title']

    def __str__(self):
        return f'{self.title}, {self.author}'

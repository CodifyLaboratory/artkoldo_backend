from django.db import models


'''
    Universal attributes
'''


class Country(models.Model):
    title = models.CharField(max_length=100, verbose_name='Страна', null=True, blank=True, unique=True)

    class Meta:
        verbose_name = 'Страна'
        verbose_name_plural = "Страны"
        ordering = ['title']

    def clean(self):
        self.title = self.title.capitalize()

    def __str__(self):
        return self.title


class Region(models.Model):
    title = models.CharField(max_length=100, verbose_name='Область', null=True, blank=True, unique=True)
    country = models.ForeignKey(Country, on_delete=models.PROTECT, verbose_name='Страна', null=True, blank=True)

    class Meta:
        verbose_name = 'Регион'
        verbose_name_plural = "Регионы"
        ordering = ['title']
        """ 
        в базу данных не будет добавлять повторяющиеся значения
        """
        unique_together = (("title", "country"),)

    def clean(self):
        self.title = self.title.capitalize()

    def __str__(self):
        return f'{self.title}, {self.country}'


class Author(models.Model):
    name = models.CharField(max_length=255, verbose_name='Ф.И. автора', null=True, blank=True)
    phone_number = models.CharField(max_length=14, verbose_name='Номер телефона', null=True, blank=True, unique=True)
    about = models.TextField(verbose_name='Об авторе', null=True, blank=True)
    region = models.ForeignKey(Region, on_delete=models.PROTECT, verbose_name='Регион', null=True, blank=True)
    created_at = models.DateTimeField(auto_now=True, verbose_name='Дата создания', blank=True, null=True)
    photo = models.ImageField(verbose_name='фото мастера', blank=True, null=True, upload_to='author photo')
    featured = models.BooleanField(blank=True, null=True, verbose_name='показанный', default=False)

    class Meta:
        verbose_name = 'Автор'
        verbose_name_plural = "Авторы"
        ordering = ['name']
        unique_together = (("name", "phone_number", "region"),)

    def clean(self):
        self.name = self.name.capitalize()

    def __str__(self):
        return self.name


class Color(models.Model):
    title = models.CharField(max_length=100, verbose_name='Цвет', null=True, blank=True, unique=True)
    code = models.CharField(max_length=7, verbose_name='Код цвета', null=True, blank=True, unique=True)

    class Meta:
        verbose_name = 'Цвет'
        verbose_name_plural = "Цвета"
        ordering = ['title']
        unique_together = (("title", "code"),)

    def clean(self):
        self.title = self.title.capitalize()

    def __str__(self):
        return self.title


'''
    Paintings
'''


class Subject(models.Model):
    title = models.CharField(max_length=100, verbose_name='Тема картины', null=True, blank=True, unique=True)

    class Meta:
        verbose_name = 'Тема картины'
        verbose_name_plural = "Темы картины"
        ordering = ['title']

    def clean(self):
        self.title = self.title.capitalize()

    def __str__(self):
        return self.title


class PaintMaterial(models.Model):
    title = models.CharField(max_length=100, verbose_name='Материал живописи', null=True, blank=True, unique=True)

    class Meta:
        verbose_name = 'Материал живописи'
        verbose_name_plural = "Материалы живописи"
        ordering = ['title']

    def clean(self):
        self.title = self.title.capitalize()

    def __str__(self):
        return self.title


class Style(models.Model):
    title = models.CharField(max_length=100, verbose_name='Стиль живописи', null=True, blank=True, unique=True)

    class Meta:
        verbose_name = 'Стиль живописи'
        verbose_name_plural = "Стили живописи"
        ordering = ['title']

    def clean(self):
        self.title = self.title.capitalize()

    def __str__(self):
        return self.title


class PaintTechnique(models.Model):
    title = models.CharField(max_length=100, verbose_name='Техника живописи', null=True, blank=True, unique=True)

    class Meta:
        verbose_name = 'Техника живописи'
        verbose_name_plural = "Техники живописи"
        ordering = ['title']

    def clean(self):
        self.title = self.title.capitalize()

    def __str__(self):
        return self.title


class Painting(models.Model):
    category = 'painting'
    title = models.CharField(max_length=100, verbose_name='Название картины', null=True, blank=True)
    photo_1 = models.ImageField(verbose_name='Фото - 1', upload_to='paintings_images', null=True, blank=True)
    photo_2 = models.ImageField(verbose_name='Фото - 2', upload_to='paintings_images', null=True, blank=True)
    photo_3 = models.ImageField(verbose_name='Фото - 3', upload_to='paintings_images', null=True, blank=True)
    photo_4 = models.ImageField(verbose_name='Фото - 4', upload_to='paintings_images', null=True, blank=True)
    description = models.TextField(max_length=500, verbose_name='Описание', null=True, blank=True)
    subject = models.ForeignKey(Subject, on_delete=models.SET_NULL, verbose_name='Тема', null=True, blank=True)
    material = models.ForeignKey(PaintMaterial, on_delete=models.SET_NULL, verbose_name='Материал', null=True, blank=True)
    style = models.ForeignKey(Style, on_delete=models.SET_NULL, verbose_name='Стиль', null=True, blank=True)
    technique = models.ForeignKey(PaintTechnique, on_delete=models.SET_NULL, verbose_name='Техника', null=True, blank=True)
    color = models.ManyToManyField(Color, verbose_name='Цвет', blank=True)
    width = models.PositiveIntegerField(verbose_name='Ширина (см)', null=True, blank=True)
    height = models.PositiveIntegerField(verbose_name='Высота (см)', null=True, blank=True)
    author = models.ForeignKey(Author, on_delete=models.SET_NULL, verbose_name='Автор', null=True, blank=True)
    price = models.PositiveIntegerField(verbose_name='Цена')
    keywords = models.CharField(max_length=100, verbose_name='Ключевые слова', null=True, blank=True)
    created_at = models.DateTimeField(auto_now=True, verbose_name='Дата создания', blank=True, null=True)
    recommended = models.BooleanField(default=False, verbose_name='Рекомендованный', blank=True, null=True)
    discount_price = models.PositiveIntegerField(verbose_name='Цена со скидкой', blank=True, null=True)

    class Meta:
        verbose_name = 'Картина'
        verbose_name_plural = 'Картины'
        ordering = ['title']
        unique_together = (
            (
                "title",
                "subject",
                "material",
                "style",
                "technique",
                "width",
                "height",
                "author"
            ),
        )

    def clean(self):
        self.title = self.title.capitalize()

    def __str__(self):
        return f'{self.title}, {self.author}'


'''
    Handicrafts
'''


class HandicraftType(models.Model):
    title = models.CharField(
        max_length=100,
        verbose_name='Тип ремесленного изделия',
        null=True,
        blank=True,
        unique=True
    )

    class Meta:
        verbose_name = 'Тип ремесленного изделия'
        verbose_name_plural = "Типы ремесленных изделий"
        ordering = ['title']

    def clean(self):
        self.title = self.title.capitalize()

    def __str__(self):
        return self.title


class HandicraftMaterial(models.Model):
    title = models.CharField(
        max_length=100,
        verbose_name='Материал ремесленного изделия',
        null=True,
        blank=True,
        unique=True
    )

    class Meta:
        verbose_name = 'Материал ремесленного изделия'
        verbose_name_plural = "Материалы ремесленных изделий"
        ordering = ['title']

    def clean(self):
        self.title = self.title.capitalize()

    def __str__(self):
        return self.title


class HandicraftTechnique(models.Model):
    title = models.CharField(max_length=100, verbose_name='Техника создания', null=True, blank=True, unique=True)

    class Meta:
        verbose_name = 'Техника ремесла'
        verbose_name_plural = "Техники ремесла"
        ordering = ['title']

    def clean(self):
        self.title = self.title.capitalize()

    def __str__(self):
        return self.title


class Handicraft(models.Model):
    category = 'handicraft'
    title = models.CharField(max_length=100, verbose_name='Название изделия', null=True, blank=True)
    photo_1 = models.ImageField(verbose_name='Фото - 1', upload_to='paintings_images', null=True, blank=True)
    photo_2 = models.ImageField(verbose_name='Фото - 2', upload_to='paintings_images', null=True, blank=True)
    photo_3 = models.ImageField(verbose_name='Фото - 3', upload_to='paintings_images', null=True, blank=True)
    photo_4 = models.ImageField(verbose_name='Фото - 4', upload_to='paintings_images', null=True, blank=True)
    description = models.TextField(max_length=500, verbose_name='Описание', null=True, blank=True)
    type = models.ForeignKey(HandicraftType, on_delete=models.SET_NULL, verbose_name='Тип изделия', null=True, blank=True)
    material = models.ForeignKey(HandicraftMaterial, on_delete=models.SET_NULL, verbose_name='Материал', null=True, blank=True)
    technique = models.ForeignKey(HandicraftTechnique, on_delete=models.SET_NULL, verbose_name='Техника', null=True, blank=True)
    color = models.ManyToManyField(Color, verbose_name='Цвет', blank=True)
    author = models.ForeignKey(Author, on_delete=models.SET_NULL, verbose_name='Автор', null=True, blank=True)
    price = models.PositiveIntegerField(verbose_name='Цена', null=True, blank=True)
    keywords = models.CharField(max_length=100, verbose_name='Ключевые слова', null=True, blank=True)
    created_at = models.DateTimeField(auto_now=True, verbose_name='Дата создания', blank=True, null=True)
    recommended = models.BooleanField(default=False, verbose_name='Рекомендованный', blank=True, null=True)
    discount_price = models.PositiveIntegerField(verbose_name='Цена со скидкой', blank=True, null=True)

    class Meta:
        verbose_name = 'Ремесленное изделие'
        verbose_name_plural = 'Ремесленные изделия'
        ordering = ['title']
        unique_together = (
            (
                "title",
                "type",
                "material",
                "technique",
                "author"
            ),
        )

    def clean(self):
        self.title = self.title.capitalize()

    def __str__(self):
        return f'{self.title}, {self.author}'


'''
    Ceramics
'''


class CeramicType(models.Model):
    title = models.CharField(max_length=100, verbose_name='Тип керамики', null=True, blank=True, unique=True)

    class Meta:
        verbose_name = 'Тип керамики'
        verbose_name_plural = "Типы керамики"
        ordering = ['title']

    def clean(self):
        self.title = self.title.capitalize()

    def __str__(self):
        return self.title


class CeramicMaterial(models.Model):
    title = models.CharField(
        max_length=100,
        verbose_name='Материал керамического изделия',
        null=True,
        blank=True,
        unique=True
    )

    class Meta:
        verbose_name = 'Материал керамического изделия'
        verbose_name_plural = "Материалы керамических изделий"
        ordering = ['title']

    def clean(self):
        self.title = self.title.capitalize()

    def __str__(self):
        return self.title


class CeramicTechnique(models.Model):
    title = models.CharField(max_length=100, verbose_name='Техника создания', null=True, blank=True, unique=True)

    class Meta:
        verbose_name = 'Техника создания керамики'
        verbose_name_plural = "Техники создания керамики"
        ordering = ['title']

    def clean(self):
        self.title = self.title.capitalize()

    def __str__(self):
        return self.title


class Ceramic(models.Model):
    category = 'ceramic'
    title = models.CharField(max_length=100, verbose_name='Название изделия', null=True, blank=True)
    photo_1 = models.ImageField(verbose_name='Фото - 1', upload_to='paintings_images', null=True, blank=True)
    photo_2 = models.ImageField(verbose_name='Фото - 2', upload_to='paintings_images', null=True, blank=True)
    photo_3 = models.ImageField(verbose_name='Фото - 3', upload_to='paintings_images', null=True, blank=True)
    photo_4 = models.ImageField(verbose_name='Фото - 4', upload_to='paintings_images', null=True, blank=True)
    description = models.TextField(max_length=500, verbose_name='Описание', null=True, blank=True)
    type = models.ForeignKey(CeramicType, on_delete=models.SET_NULL, verbose_name='Тип изделия', null=True, blank=True)
    material = models.ForeignKey(CeramicMaterial, on_delete=models.SET_NULL, verbose_name='Материал', null=True, blank=True)
    technique = models.ForeignKey(CeramicTechnique, on_delete=models.SET_NULL, verbose_name='Техника', null=True, blank=True)
    color = models.ManyToManyField(Color, verbose_name='Цвет', blank=True)
    author = models.ForeignKey(Author, on_delete=models.SET_NULL, verbose_name='Автор', null=True, blank=True)
    price = models.PositiveIntegerField(verbose_name='Цена', null=True, blank=True)
    keywords = models.CharField(max_length=100, verbose_name='Ключевые слова', null=True, blank=True)
    created_at = models.DateTimeField(auto_now=True, verbose_name='Дата создания', blank=True, null=True)
    recommended = models.BooleanField(default=False, verbose_name='Рекомендованный', blank=True, null=True)
    discount_price = models.PositiveIntegerField(verbose_name='Цена со скидкой', blank=True, null=True)

    class Meta:
        verbose_name = 'Керамика'
        verbose_name_plural = 'Керамика'
        ordering = ['title']
        unique_together = (
            (
                "title",
                "description",
                "type",
                "material",
                "technique",
                "author"
            ),
        )

    def clean(self):
        self.title = self.title.capitalize()

    def __str__(self):
        return f'{self.title}, {self.author}'

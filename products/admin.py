from django.contrib import admin
from django.utils.safestring import mark_safe

from .models import Country, Region, Author, Color
from .models import Subject, PaintMaterial, Style, PaintTechnique, Painting
from .models import HandicraftType, HandicraftMaterial, HandicraftTechnique, Handicraft
from .models import CeramicType, CeramicMaterial, CeramicTechnique, Ceramic


class SiteAdmin(admin.ModelAdmin):
    readonly_fields = ('id',)


class AuthorAdmin(admin.ModelAdmin):
    readonly_fields = ('id', 'created_at', 'get_html_photo',)
    list_display = ('name', 'id', 'region', 'get_html_photo', 'featured')
    list_filter = ('name', 'region__country')
    fields = ('name', 'phone_number', 'about', 'region', 'photo', 'get_html_photo', 'featured')
    list_editable = ('featured',)

    def get_html_photo(self, object):
        if object.photo:
            return mark_safe(f"<img src='{object.photo.url}' width=50>")

    get_html_photo.short_description = 'фото мастера'


class CountryAdmin(admin.ModelAdmin):
    readonly_fields = ('id',)
    list_filter = ('country',)


class PaintingAdmin(admin.ModelAdmin):
    list_display = ('title', 'id', 'author', 'recommended', 'created_at', 'get_html_photo')
    readonly_fields = ('id', 'created_at')
    list_editable = ('recommended',)

    fieldsets = (
        ('Общая информация', {
            'fields': (
                'id',
                'title',
                'photo_1',
                'photo_2',
                'photo_3',
                'photo_4',
                'description',
                'author',
                'price'
            )
        }),
        ('Характеристики', {
            'fields': ('subject', 'material', 'style', 'technique', 'color', ('width', 'height')),
        }),
        ('Дополнительно', {
            'fields': ('keywords', 'recommended', 'discount_price', 'created_at'),
        })
    )

    list_filter = ('recommended', 'author', 'author__region', 'color')

    def get_html_photo(self, object):
        if object.photo_1:
            return mark_safe(f"<img src='{object.photo_1.url}' width=50>")

    get_html_photo.short_description = 'Фото - 1'


class HandicraftCeramicAdmin(admin.ModelAdmin):
    list_display = ('title', 'id', 'author', 'recommended', 'created_at', 'get_html_photo')
    readonly_fields = ('id', 'created_at')
    list_editable = ('recommended',)

    fieldsets = (
        ('Общая информация', {
            'fields': (
                'id',
                'title',
                'photo_1',
                'photo_2',
                'photo_3',
                'photo_4',
                'description',
                'author',
                'price'
            )
        }),
        ('Характеристики', {
            'fields': ('type', 'material', 'technique', 'color',),
        }),
        ('Дополнительно', {
            'fields': ('keywords', 'recommended', 'discount_price', 'created_at'),
        })
    )

    list_filter = ('recommended', 'author', 'author__region', 'color')

    def get_html_photo(self, object):
        if object.photo_1:
            return mark_safe(f"<img src='{object.photo_1.url}' width=50>")

    get_html_photo.short_description = 'Фото - 1'


""" Общие """
admin.site.register(Country, SiteAdmin)
admin.site.register(Region, CountryAdmin)
admin.site.register(Author, AuthorAdmin)
admin.site.register(Color, SiteAdmin)

""" Живопись """
admin.site.register(Subject, SiteAdmin)
admin.site.register(PaintMaterial, SiteAdmin)
admin.site.register(Style, SiteAdmin)
admin.site.register(PaintTechnique, SiteAdmin)
admin.site.register(Painting, PaintingAdmin)

""" Ремесленные изделия """
admin.site.register(HandicraftType, SiteAdmin)
admin.site.register(HandicraftMaterial, SiteAdmin)
admin.site.register(HandicraftTechnique, SiteAdmin)
admin.site.register(Handicraft, HandicraftCeramicAdmin)

""" Керамика """
admin.site.register(CeramicType, SiteAdmin)
admin.site.register(CeramicMaterial, SiteAdmin)
admin.site.register(CeramicTechnique, SiteAdmin)
admin.site.register(Ceramic, HandicraftCeramicAdmin)

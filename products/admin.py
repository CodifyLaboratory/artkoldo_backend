from django.contrib import admin
from .models import Country, Region, Author, Color
from .models import Subject, PaintMaterial, Style, PaintTechnique, Painting
from .models import HandicraftType, HandicraftMaterial, HandicraftTechnique, Handicraft
from .models import CeramicType, CeramicMaterial, CeramicTechnique, Ceramic


class SiteAdmin(admin.ModelAdmin):
    readonly_fields = ('id',)


class AuthorAdmin(admin.ModelAdmin):
    readonly_fields = ('id', 'created_at')
    list_display = ('name', 'id', 'region',)
    list_filter = ('name', 'region__country')


class CountryAdmin(admin.ModelAdmin):
    readonly_fields = ('id',)
    list_filter = ('country',)


class PaintingAdmin(admin.ModelAdmin):
    list_display = ('title', 'id', 'author', 'recommended', 'created_at')
    readonly_fields = ('id', 'created_at')

    fieldsets = (
        ('Общая информация', {
            'fields': (
                'id',
                'title',
                'photo_1',
                'photo_2',
                'photo_3',
                'photo_4',
                'photo_5',
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


class HandicraftCeramicAdmin(admin.ModelAdmin):
    list_display = ('title', 'id', 'author', 'recommended', 'created_at')
    readonly_fields = ('id', 'created_at')

    fieldsets = (
        ('Общая информация', {
            'fields': (
                'id',
                'title',
                'photo_1',
                'photo_2',
                'photo_3',
                'photo_4',
                'photo_5',
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

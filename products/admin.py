from django.contrib import admin
from .models import Country, Region, Author, Color
from .models import Subject, PaintMaterial, Style, PaintTechnique, Painting
from .models import HandicraftType, HandicraftMaterial, HandicraftTechnique, Handicraft
from .models import CeramicType, CeramicMaterial, CeramicTechnique, Ceramic


class SiteAdmin(admin.ModelAdmin):
    readonly_fields = ('id',)


class AuthorAdmin(admin.ModelAdmin):
    readonly_fields = ('id', 'created_at')
    list_display = ('id', 'name', 'region',)


class CountryAdmin(admin.ModelAdmin):
    readonly_fields = ('id',)
    list_filter = ('country',)


class ProductAdmin(admin.ModelAdmin):
    readonly_fields = ('id', 'created_at',)


admin.site.register(Country, SiteAdmin)
admin.site.register(Region, CountryAdmin)
admin.site.register(Author, AuthorAdmin)
admin.site.register(Color, SiteAdmin)

admin.site.register(Subject, SiteAdmin)
admin.site.register(PaintMaterial, SiteAdmin)
admin.site.register(Style, SiteAdmin)
admin.site.register(PaintTechnique, SiteAdmin)
admin.site.register(Painting, ProductAdmin)

admin.site.register(HandicraftType, SiteAdmin)
admin.site.register(HandicraftMaterial, SiteAdmin)
admin.site.register(HandicraftTechnique, SiteAdmin)
admin.site.register(Handicraft, ProductAdmin)

admin.site.register(CeramicType, SiteAdmin)
admin.site.register(CeramicMaterial, SiteAdmin)
admin.site.register(CeramicTechnique, SiteAdmin)
admin.site.register(Ceramic, ProductAdmin)

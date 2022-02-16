from django.contrib import admin
from .models import Origin, Author, Color
from .models import Subject, PaintMaterial, Style, PaintTechnique, Painting
from .models import HandicraftType, HandicraftMaterial, HandicraftTechnique, Handicraft
from .models import CeramicType, CeramicMaterial, CeramicTechnique, Ceramic

class SiteAdmin(admin.ModelAdmin):
    readonly_fields = ('id',)


admin.site.register(Origin, SiteAdmin)
admin.site.register(Author, SiteAdmin)
admin.site.register(Color, SiteAdmin)

admin.site.register(Subject, SiteAdmin)
admin.site.register(PaintMaterial, SiteAdmin)
admin.site.register(Style, SiteAdmin)
admin.site.register(PaintTechnique, SiteAdmin)
admin.site.register(Painting, SiteAdmin)

admin.site.register(HandicraftType, SiteAdmin)
admin.site.register(HandicraftMaterial, SiteAdmin)
admin.site.register(HandicraftTechnique, SiteAdmin)
admin.site.register(Handicraft, SiteAdmin)

admin.site.register(CeramicType, SiteAdmin)
admin.site.register(CeramicMaterial, SiteAdmin)
admin.site.register(CeramicTechnique, SiteAdmin)
admin.site.register(Ceramic, SiteAdmin)

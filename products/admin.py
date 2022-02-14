from django.contrib import admin
from .models import Origin, Author, Color
from .models import Subject, PaintMaterial, Style, PaintTechnique, Painting
from .models import HandicraftType, HandicraftMaterial, HandicraftTechnique, Handicraft
from .models import CeramicType, CeramicMaterial, CeramicTechnique, Ceramic


admin.site.register(Origin)
admin.site.register(Author)
admin.site.register(Color)

admin.site.register(Painting)
admin.site.register(Subject)
admin.site.register(PaintMaterial)
admin.site.register(Style)
admin.site.register(PaintTechnique)

admin.site.register(HandicraftType)
admin.site.register(HandicraftMaterial)
admin.site.register(HandicraftTechnique)
admin.site.register(Handicraft)

admin.site.register(CeramicType)
admin.site.register(CeramicMaterial)
admin.site.register(CeramicTechnique)
admin.site.register(Ceramic)

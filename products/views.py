from rest_framework import viewsets
from drf_multiple_model.viewsets import ObjectMultipleModelAPIViewSet

from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter, OrderingFilter
from .filters import PaintingFilter

from .models import Region, Author, Color, \
    Subject, PaintMaterial, Style, PaintTechnique, Painting, \
    HandicraftType, HandicraftMaterial, HandicraftTechnique, Handicraft, \
    CeramicType, CeramicMaterial, CeramicTechnique, Ceramic
from .serializers import RegionSerializer, AuthorSerializer, ColorSerializer, \
    SubjectSerializer, PaintMaterialSerializer, StyleSerializer, PaintTechniqueSerializer, PaintingSerializer, \
    HandicraftTypeSerializer, HandicraftMaterialSerializer, HandicraftTechniqueSerializer, HandicraftSerializer, \
    CeramicTypeSerializer, CeramicMaterialSerializer, CeramicTechniqueSerializer, CeramicSerializer


class PaintingViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Painting.objects.all()
    serializer_class = PaintingSerializer

    filterset_class = PaintingFilter
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    search_fields = ['title', 'description', 'color__title', 'author__region__country__title', 'author__region__title',
                     'author__name', 'keywords', 'style__title', 'subject__title', 'technique__title', 'material__title']
    ordering_fields = ['price']


class PaintingFilterViewSet(ObjectMultipleModelAPIViewSet):
    querylist = [
        {'queryset': Subject.objects.all(), 'serializer_class': SubjectSerializer},
        {'queryset': PaintMaterial.objects.all(), 'serializer_class': PaintMaterialSerializer},
        {'queryset': Style.objects.all(), 'serializer_class': StyleSerializer},
        {'queryset': PaintTechnique.objects.all(), 'serializer_class': PaintTechniqueSerializer},
        {'queryset': Color.objects.all(), 'serializer_class': ColorSerializer},
        {'queryset': Region.objects.all(), 'serializer_class': RegionSerializer},
    ]


class HandicraftViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Handicraft.objects.all()
    serializer_class = HandicraftSerializer


class CeramicViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Ceramic.objects.all()
    serializer_class = CeramicSerializer


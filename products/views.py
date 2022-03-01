from rest_framework import viewsets
from .pagination import ProductsPagination
from drf_multiple_model.viewsets import ObjectMultipleModelAPIViewSet

from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter, OrderingFilter
from .filters import PaintingFilter, HandicraftFilter, CeramicFilter

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
    pagination_class = ProductsPagination

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
    pagination_class = ProductsPagination

    filterset_class = HandicraftFilter
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    search_fields = ['title', 'description', 'color__title', 'author__region__country__title', 'author__region__title',
                     'author__name', 'keywords', 'type__title', 'technique__title', 'material__title']
    ordering_fields = ['price']


class HandicraftFilterViewSet(ObjectMultipleModelAPIViewSet):
    querylist = [
        {'queryset': HandicraftType.objects.all(), 'serializer_class': HandicraftTypeSerializer},
        {'queryset': HandicraftMaterial.objects.all(), 'serializer_class': HandicraftMaterialSerializer},
        {'queryset': HandicraftTechnique.objects.all(), 'serializer_class': HandicraftTechniqueSerializer},
        {'queryset': Color.objects.all(), 'serializer_class': ColorSerializer},
        {'queryset': Region.objects.all(), 'serializer_class': RegionSerializer},
    ]


class CeramicViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Ceramic.objects.all()
    serializer_class = CeramicSerializer
    pagination_class = ProductsPagination

    filterset_class = CeramicFilter
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    search_fields = ['title', 'description', 'color__title', 'author__region__country__title', 'author__region__title',
                     'author__name', 'keywords', 'type__title', 'technique__title', 'material__title']
    ordering_fields = ['price']


class CeramicFilterViewSet(ObjectMultipleModelAPIViewSet):
    querylist = [
        {'queryset': CeramicType.objects.all(), 'serializer_class': CeramicTypeSerializer},
        {'queryset': CeramicMaterial.objects.all(), 'serializer_class': CeramicMaterialSerializer},
        {'queryset': CeramicTechnique.objects.all(), 'serializer_class': CeramicTechniqueSerializer},
        {'queryset': Color.objects.all(), 'serializer_class': ColorSerializer},
        {'queryset': Region.objects.all(), 'serializer_class': RegionSerializer},
    ]

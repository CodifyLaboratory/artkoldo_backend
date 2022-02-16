from django.shortcuts import render
from rest_framework.viewsets import ReadOnlyModelViewSet
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter, OrderingFilter
from .filters import PaintingFilter


from .models import Origin, Author, Color, \
    Subject, PaintMaterial, Style, PaintTechnique, Painting, \
    HandicraftType, HandicraftMaterial, HandicraftTechnique, Handicraft, \
    CeramicType, CeramicMaterial, CeramicTechnique, Ceramic
from .serializers import OriginSerializer, AuthorSerializer, ColorSerializer, \
    SubjectSerializer, PaintMaterialSerializer, StyleSerializer, PaintTechniqueSerializer, PaintingSerializer, \
    HandicraftTypeSerializer, HandicraftMaterialSerializer, HandicraftTechniqueSerializer, HandicraftSerializer, \
    CeramicTypeSerializer, CeramicMaterialSerializer, CeramicTechniqueSerializer, CeramicSerializer


class OriginViewSet(ReadOnlyModelViewSet):
    queryset = Origin.objects.all()
    serializer_class = OriginSerializer


class AuthorViewSet(ReadOnlyModelViewSet):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer


class ColorViewSet(ReadOnlyModelViewSet):
    queryset = Color.objects.all()
    serializer_class = ColorSerializer


'''
    Paintings
'''
class SubjectViewSet(ReadOnlyModelViewSet):
    queryset = Subject.objects.all()
    serializer_class = SubjectSerializer


class PaintMaterialViewSet(ReadOnlyModelViewSet):
    queryset = PaintMaterial.objects.all()
    serializer_class = PaintMaterialSerializer


class StyleViewSet(ReadOnlyModelViewSet):
    queryset = Style.objects.all()
    serializer_class = StyleSerializer


class PaintTechniqueViewSet(ReadOnlyModelViewSet):
    queryset = PaintTechnique.objects.all()
    serializer_class = PaintTechniqueSerializer


class PaintingViewSet(ReadOnlyModelViewSet):
    queryset = Painting.objects.all()
    serializer_class = PaintingSerializer
    filterset_class = PaintingFilter
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    search_fields = ['title', 'description', 'color__title', 'author__origin__country', 'author__origin__region',
                     'author__name', 'keywords', 'style__title', 'subject__title', 'technique__title', 'material__title']
    ordering_fields = ['price']


'''
    Handicrafts
'''
class HandicraftTypeViewSet(ReadOnlyModelViewSet):
    queryset = HandicraftType.objects.all()
    serializer_class = HandicraftTypeSerializer


class HandicraftMaterialViewSet(ReadOnlyModelViewSet):
    queryset = HandicraftMaterial.objects.all()
    serializer_class = HandicraftMaterialSerializer


class HandicraftTechniqueViewSet(ReadOnlyModelViewSet):
    queryset = HandicraftTechnique.objects.all()
    serializer_class = HandicraftTechniqueSerializer


class HandicraftViewSet(ReadOnlyModelViewSet):
    queryset = Handicraft.objects.all()
    serializer_class = HandicraftSerializer
    # filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    # filterset_fields = ['type', 'material', 'technique', 'color']
    # search_fields = ['title', 'type__title', 'material__title', 'description', 'color__title', 'keywords', 'technique__title']
    # ordering_fields = ['price']


'''
    Ceramics
'''
class CeramicTypeViewSet(ReadOnlyModelViewSet):
    queryset = CeramicType.objects.all()
    serializer_class = CeramicTypeSerializer


class CeramicMaterialViewSet(ReadOnlyModelViewSet):
    queryset = CeramicMaterial.objects.all()
    serializer_class = CeramicMaterialSerializer


class CeramicTechniqueViewSet(ReadOnlyModelViewSet):
    queryset = CeramicTechnique.objects.all()
    serializer_class = CeramicTechniqueSerializer


class CeramicViewSet(ReadOnlyModelViewSet):
    queryset = Ceramic.objects.all()
    serializer_class = CeramicSerializer
    # filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    # filterset_fields = ['type', 'material', 'technique', 'color']
    # search_fields = ['title', 'type__title', 'material__title', 'description', 'color__title', 'keywords', 'technique__title']
    # ordering_fields = ['price']

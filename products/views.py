from itertools import chain

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
    CeramicTypeSerializer, CeramicMaterialSerializer, CeramicTechniqueSerializer, CeramicSerializer, \
    PaintingDetailSerializer, HandicraftDetailSerializer, CeramicDetailSerializer


class PaintingViewSet(viewsets.ReadOnlyModelViewSet):
    """ Каталог Живописи """
    queryset = Painting.objects.all().order_by('-id')
    serializer_class = PaintingSerializer
    pagination_class = ProductsPagination

    filterset_class = PaintingFilter
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    search_fields = ['title', 'description', 'color__title', 'author__region__country__title', 'author__region__title',
                     'author__name', 'keywords', 'style__title', 'subject__title', 'technique__title', 'material__title']
    ordering_fields = ['price', 'created_at']


class PaintingFilterViewSet(ObjectMultipleModelAPIViewSet):
    """ Параметры фильтрации Живописи """
    querylist = [
        {'queryset': Subject.objects.all(), 'serializer_class': SubjectSerializer},
        {'queryset': PaintMaterial.objects.all(), 'serializer_class': PaintMaterialSerializer},
        {'queryset': Style.objects.all(), 'serializer_class': StyleSerializer},
        {'queryset': PaintTechnique.objects.all(), 'serializer_class': PaintTechniqueSerializer},
        {'queryset': Color.objects.all(), 'serializer_class': ColorSerializer},
        {'queryset': Region.objects.all(), 'serializer_class': RegionSerializer},
    ]


class PaintingDetailViewSet(viewsets.ReadOnlyModelViewSet):
    serializer_class = PaintingDetailSerializer

    def get_queryset(self):
        queryset = Painting.objects.filter(id=self.kwargs['pk'])
        return queryset


class PaintingRecommendationsViewSet(viewsets.ReadOnlyModelViewSet):
    serializer_class = PaintingSerializer

    def get_queryset(self):
        exclude = [self.kwargs['pk']]
        reference = Painting.objects.get(id=self.kwargs['pk'])
        same_author = Painting.objects.filter(author=reference.author).exclude(id__in=exclude)
        for product in same_author: exclude.append(product.id)
        same_subject = Painting.objects.filter(subject=reference.subject).exclude(id__in=exclude)
        for product in same_subject: exclude.append(product.id)
        same_style = Painting.objects.filter(style=reference.style).exclude(id__in=exclude)
        for product in same_style: exclude.append(product.id)
        same_technique = Painting.objects.filter(technique=reference.technique).exclude(id__in=exclude)
        for product in same_technique: exclude.append(product.id)
        queryset = chain(same_author, same_subject, same_style, same_technique)
        return queryset


class HandicraftViewSet(viewsets.ReadOnlyModelViewSet):
    """ Каталог Ремесленных изделий """
    queryset = Handicraft.objects.all().order_by('-id')
    serializer_class = HandicraftSerializer
    pagination_class = ProductsPagination

    filterset_class = HandicraftFilter
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    search_fields = ['title', 'description', 'color__title', 'author__region__country__title', 'author__region__title',
                     'author__name', 'keywords', 'type__title', 'technique__title', 'material__title']
    ordering_fields = ['price', 'created_at']


class HandicraftFilterViewSet(ObjectMultipleModelAPIViewSet):
    """ Параметры фильтрации Ремесленных изделий """
    querylist = [
        {'queryset': HandicraftType.objects.all(), 'serializer_class': HandicraftTypeSerializer},
        {'queryset': HandicraftMaterial.objects.all(), 'serializer_class': HandicraftMaterialSerializer},
        {'queryset': HandicraftTechnique.objects.all(), 'serializer_class': HandicraftTechniqueSerializer},
        {'queryset': Color.objects.all(), 'serializer_class': ColorSerializer},
        {'queryset': Region.objects.all(), 'serializer_class': RegionSerializer},
    ]


class HandicraftDetailViewSet(viewsets.ReadOnlyModelViewSet):
    serializer_class = HandicraftDetailSerializer

    def get_queryset(self):
        queryset = Handicraft.objects.filter(id=self.kwargs['pk'])
        return queryset


class HandicraftRecommendationsViewSet(viewsets.ReadOnlyModelViewSet):
    serializer_class = HandicraftSerializer

    def get_queryset(self):
        exclude = [self.kwargs['pk']]
        reference = Handicraft.objects.get(id=self.kwargs['pk'])
        same_author = Handicraft.objects.filter(author=reference.author).exclude(id__in=exclude)
        for product in same_author: exclude.append(product.id)
        same_type = Handicraft.objects.filter(type=reference.type).exclude(id__in=exclude)
        for product in same_type: exclude.append(product.id)
        same_material = Handicraft.objects.filter(material=reference.material).exclude(id__in=exclude)
        for product in same_material: exclude.append(product.id)
        same_technique = Handicraft.objects.filter(technique=reference.technique).exclude(id__in=exclude)
        for product in same_technique: exclude.append(product.id)
        queryset = chain(same_author, same_type, same_material, same_technique)
        return queryset


class CeramicViewSet(viewsets.ReadOnlyModelViewSet):
    """ Каталог Керамики """
    queryset = Ceramic.objects.all().order_by('-id')
    serializer_class = CeramicSerializer
    pagination_class = ProductsPagination

    filterset_class = CeramicFilter
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    search_fields = ['title', 'description', 'color__title', 'author__region__country__title', 'author__region__title',
                     'author__name', 'keywords', 'type__title', 'technique__title', 'material__title']
    ordering_fields = ['price', 'created_at']


class CeramicFilterViewSet(ObjectMultipleModelAPIViewSet):
    """ Параметры фильтрации Керамики """
    querylist = [
        {'queryset': CeramicType.objects.all(), 'serializer_class': CeramicTypeSerializer},
        {'queryset': CeramicMaterial.objects.all(), 'serializer_class': CeramicMaterialSerializer},
        {'queryset': CeramicTechnique.objects.all(), 'serializer_class': CeramicTechniqueSerializer},
        {'queryset': Color.objects.all(), 'serializer_class': ColorSerializer},
        {'queryset': Region.objects.all(), 'serializer_class': RegionSerializer},
    ]


class CeramicDetailViewSet(viewsets.ReadOnlyModelViewSet):
    serializer_class = CeramicDetailSerializer

    def get_queryset(self):
        queryset = Ceramic.objects.filter(id=self.kwargs['pk'])
        return queryset


class CeramicRecommendationsViewSet(viewsets.ReadOnlyModelViewSet):
    serializer_class = CeramicSerializer

    def get_queryset(self):
        exclude = [self.kwargs['pk']]
        reference = Ceramic.objects.get(id=self.kwargs['pk'])
        same_author = Ceramic.objects.filter(author=reference.author).exclude(id__in=exclude)
        for product in same_author: exclude.append(product.id)
        same_type = Ceramic.objects.filter(type=reference.type).exclude(id__in=exclude)
        for product in same_type: exclude.append(product.id)
        same_material = Ceramic.objects.filter(material=reference.material).exclude(id__in=exclude)
        for product in same_material: exclude.append(product.id)
        same_technique = Ceramic.objects.filter(technique=reference.technique).exclude(id__in=exclude)
        for product in same_technique: exclude.append(product.id)
        queryset = chain(same_author, same_type, same_material, same_technique)
        return queryset

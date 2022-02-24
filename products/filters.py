from django.forms import CheckboxSelectMultiple
from django_filters import rest_framework as filters
from .models import Region, Color, \
    Subject, PaintMaterial, Style, PaintTechnique, Painting, \
    HandicraftType, HandicraftMaterial, HandicraftTechnique, Handicraft, \
    CeramicType, CeramicMaterial, CeramicTechnique, Ceramic


class PaintingFilter(filters.FilterSet):
    subject = filters.ModelMultipleChoiceFilter(queryset=Subject.objects.all(), widget=CheckboxSelectMultiple(), label="Тема")
    material = filters.ModelMultipleChoiceFilter(queryset=PaintMaterial.objects.all(), widget=CheckboxSelectMultiple(), label="Материал")
    style = filters.ModelMultipleChoiceFilter(queryset=Style.objects.all(), widget=CheckboxSelectMultiple(), label="Стиль")
    technique = filters.ModelMultipleChoiceFilter(queryset=PaintTechnique.objects.all(), widget=CheckboxSelectMultiple(), label="Техника")
    color = filters.ModelMultipleChoiceFilter(queryset=Color.objects.all(), widget=CheckboxSelectMultiple(), label="Цвет")
    min_width = filters.NumberFilter(field_name="width", lookup_expr='gte', label='Ширина мин.')
    max_width = filters.NumberFilter(field_name="width", lookup_expr='lte', label='Ширина макс.')
    min_height = filters.NumberFilter(field_name="height", lookup_expr='gte', label='Высота мин.')
    max_height = filters.NumberFilter(field_name="height", lookup_expr='lte', label='Высота макс.')
    min_price = filters.NumberFilter(field_name="price", lookup_expr='gte', label='Цена мин.')
    max_price = filters.NumberFilter(field_name="price", lookup_expr='lte', label='Цена макс.')
    author__region = filters.ModelMultipleChoiceFilter(queryset=Region.objects.all(), widget=CheckboxSelectMultiple(), label="Регион")

    class Meta:
        model = Painting
        fields = ['subject', 'material', 'style', 'technique', 'color', 'min_price', 'max_price', 'min_width',
                  'max_width', 'min_height', 'max_height', 'author__region']


class HandicraftFilter(filters.FilterSet):
    type = filters.ModelMultipleChoiceFilter(queryset=HandicraftType.objects.all(), widget=CheckboxSelectMultiple(), label="Тип товара")
    material = filters.ModelMultipleChoiceFilter(queryset=HandicraftMaterial.objects.all(), widget=CheckboxSelectMultiple(), label="Материал")
    technique = filters.ModelMultipleChoiceFilter(queryset=HandicraftTechnique.objects.all(), widget=CheckboxSelectMultiple(), label="Техника")
    color = filters.ModelMultipleChoiceFilter(queryset=Color.objects.all(), widget=CheckboxSelectMultiple(), label="Цвет")
    min_price = filters.NumberFilter(field_name="price", lookup_expr='gte', label='Цена мин.')
    max_price = filters.NumberFilter(field_name="price", lookup_expr='lte', label='Цена макс.')
    author__region = filters.ModelMultipleChoiceFilter(queryset=Region.objects.all(), widget=CheckboxSelectMultiple(), label="Регион")

    class Meta:
        model = Handicraft
        fields = ['type', 'material', 'technique', 'color', 'min_price', 'max_price', 'author__region']


class CeramicFilter(filters.FilterSet):
    type = filters.ModelMultipleChoiceFilter(queryset=CeramicType.objects.all(), widget=CheckboxSelectMultiple(), label="Тип товара")
    material = filters.ModelMultipleChoiceFilter(queryset=CeramicMaterial.objects.all(), widget=CheckboxSelectMultiple(), label="Материал")
    technique = filters.ModelMultipleChoiceFilter(queryset=CeramicTechnique.objects.all(), widget=CheckboxSelectMultiple(), label="Техника")
    color = filters.ModelMultipleChoiceFilter(queryset=Color.objects.all(), widget=CheckboxSelectMultiple(), label="Цвет")
    min_price = filters.NumberFilter(field_name="price", lookup_expr='gte', label='Цена мин.')
    max_price = filters.NumberFilter(field_name="price", lookup_expr='lte', label='Цена макс.')
    author__region = filters.ModelMultipleChoiceFilter(queryset=Region.objects.all(), widget=CheckboxSelectMultiple(), label="Регион")

    class Meta:
        model = Ceramic
        fields = ['type', 'material', 'technique', 'color', 'min_price', 'max_price', 'author__region']

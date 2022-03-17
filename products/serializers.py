from rest_framework import serializers
from .models import Country, Region, Author, Color, \
    Subject, PaintMaterial, Style, PaintTechnique, Painting, \
    HandicraftType, HandicraftMaterial, HandicraftTechnique, Handicraft, \
    CeramicType, CeramicMaterial, CeramicTechnique, Ceramic


class CountrySerializer(serializers.ModelSerializer):

    class Meta:
        model = Country
        fields = ['title']


class RegionSerializer(serializers.ModelSerializer):
    country = CountrySerializer()

    class Meta:
        model = Region
        fields = ['id', 'title', 'country']


class AuthorSerializer(serializers.ModelSerializer):
    region = RegionSerializer()
    created_at = serializers.ReadOnlyField()

    class Meta:
        model = Author
        fields = ['name', 'about', 'region', 'created_at']


class ColorSerializer(serializers.ModelSerializer):

    class Meta:
        model = Color
        fields = ['id', 'title', 'code']


'''
    Paintings
'''

class SubjectSerializer(serializers.ModelSerializer):

    class Meta:
        model = Subject
        fields = ['id', 'title']


class PaintMaterialSerializer(serializers.ModelSerializer):

    class Meta:
        model = PaintMaterial
        fields = ['id', 'title']


class StyleSerializer(serializers.ModelSerializer):

    class Meta:
        model = Style
        fields = ['id', 'title']


class PaintTechniqueSerializer(serializers.ModelSerializer):

    class Meta:
        model = PaintTechnique
        fields = ['id', 'title']


class PaintingSerializer(serializers.ModelSerializer):
    subject = SubjectSerializer()
    material = PaintMaterialSerializer()
    style = StyleSerializer()
    technique = PaintTechniqueSerializer()
    color = ColorSerializer(many=True)
    author = AuthorSerializer()
    created_at = serializers.ReadOnlyField()

    class Meta:
        model = Painting
        fields = ['id', 'category', 'title', 'photo', 'description', 'keywords', 'width', 'height', 'price', 'subject', 'material',
                  'style', 'technique', 'color', 'author', 'created_at', 'recommended', 'discount_price']


'''
    Handicrafts
'''

class HandicraftTypeSerializer(serializers.ModelSerializer):

    class Meta:
        model = HandicraftType
        fields = ['id', 'title']


class HandicraftMaterialSerializer(serializers.ModelSerializer):

    class Meta:
        model = HandicraftMaterial
        fields = ['id', 'title']


class HandicraftTechniqueSerializer(serializers.ModelSerializer):

    class Meta:
        model = HandicraftTechnique
        fields = ['id', 'title']


class HandicraftSerializer(serializers.ModelSerializer):
    type = HandicraftTypeSerializer()
    material = HandicraftMaterialSerializer()
    technique = HandicraftTechniqueSerializer()
    color = ColorSerializer(many=True)
    author = AuthorSerializer()
    created_at = serializers.ReadOnlyField()

    class Meta:
        model = Handicraft
        fields = ['id', 'category', 'title', 'photo', 'description', 'keywords', 'price', 'type', 'material', 'technique',
                  'color', 'author', 'created_at', 'recommended', 'discount_price']


'''
    Ceramics
'''

class CeramicTypeSerializer(serializers.ModelSerializer):

    class Meta:
        model = CeramicType
        fields = ['id', 'title']


class CeramicMaterialSerializer(serializers.ModelSerializer):

    class Meta:
        model = CeramicMaterial
        fields = ['id', 'title']


class CeramicTechniqueSerializer(serializers.ModelSerializer):

    class Meta:
        model = CeramicTechnique
        fields = ['id', 'title']


class CeramicSerializer(serializers.ModelSerializer):
    type = CeramicTypeSerializer()
    material = CeramicMaterialSerializer()
    technique = CeramicTechniqueSerializer()
    color = ColorSerializer(many=True)
    author = AuthorSerializer()
    created_at = serializers.ReadOnlyField()

    class Meta:
        model = Ceramic
        fields = ['id', 'category', 'title', 'photo', 'description', 'keywords', 'price', 'type', 'material', 'technique',
                  'color', 'author', 'created_at', 'recommended', 'discount_price']

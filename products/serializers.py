from rest_framework import serializers
from .models import Region, Author, Color, \
    Subject, PaintMaterial, Style, PaintTechnique, Painting, \
    HandicraftType, HandicraftMaterial, HandicraftTechnique, Handicraft, \
    CeramicType, CeramicMaterial, CeramicTechnique, Ceramic


class RegionSerializer(serializers.ModelSerializer):

    class Meta:
        model = Region
        fields = ['country', 'region']


class AuthorSerializer(serializers.ModelSerializer):

    class Meta:
        model = Author
        fields = ['name', 'about', 'origin']


class ColorSerializer(serializers.ModelSerializer):

    class Meta:
        model = Color
        fields = ['title', 'code']


'''
    Paintings
'''
class SubjectSerializer(serializers.ModelSerializer):

    class Meta:
        model = Subject
        fields = ['title']


class PaintMaterialSerializer(serializers.ModelSerializer):

    class Meta:
        model = PaintMaterial
        fields = ['title']


class StyleSerializer(serializers.ModelSerializer):

    class Meta:
        model = Style
        fields = ['title']


class PaintTechniqueSerializer(serializers.ModelSerializer):

    class Meta:
        model = PaintTechnique
        fields = ['title']


class PaintingSerializer(serializers.ModelSerializer):

    class Meta:
        model = Painting
        fields = '__all__'


'''
    Handicrafts
'''
class HandicraftTypeSerializer(serializers.ModelSerializer):

    class Meta:
        model = HandicraftType
        fields = ['title']


class HandicraftMaterialSerializer(serializers.ModelSerializer):

    class Meta:
        model = HandicraftMaterial
        fields = ['title']


class HandicraftTechniqueSerializer(serializers.ModelSerializer):

    class Meta:
        model = HandicraftTechnique
        fields = ['title']


class HandicraftSerializer(serializers.ModelSerializer):

    class Meta:
        model = Handicraft
        fields = '__all__'


'''
    Ceramics
'''
class CeramicTypeSerializer(serializers.ModelSerializer):

    class Meta:
        model = CeramicType
        fields = ['title']


class CeramicMaterialSerializer(serializers.ModelSerializer):

    class Meta:
        model = CeramicMaterial
        fields = ['title']


class CeramicTechniqueSerializer(serializers.ModelSerializer):

    class Meta:
        model = CeramicTechnique
        fields = ['title']


class CeramicSerializer(serializers.ModelSerializer):

    class Meta:
        model = Ceramic
        fields = '__all__'

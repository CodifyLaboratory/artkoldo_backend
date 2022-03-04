from rest_framework import serializers
from .models import PaintingOrder, HandicraftOrder, CeramicOrder
from products.models import Painting, Handicraft, Ceramic
from products.serializers import PaintingSerializer, HandicraftSerializer, CeramicSerializer


class PaintingOrderSerializer(serializers.ModelSerializer):
    price = serializers.ReadOnlyField()
    total_sum = serializers.ReadOnlyField()
    order_status = serializers.ReadOnlyField()
    created = serializers.ReadOnlyField()

    class Meta:
        model = PaintingOrder
        fields = '__all__'

    def create(self, validated_data):
        product = validated_data.get('product')
        product = Painting.objects.get(id=product.id)
        total_sum = validated_data['quantity'] * product.price
        price = product.price
        order = PaintingOrder.objects.create(
            price=price,
            total_sum=total_sum,
            customer_name=validated_data['customer_name'],
            phone_number=validated_data['phone_number'],
            product=validated_data['product'],
            quantity=validated_data['quantity'],
        )
        return order

    def to_representation(self, instance):
        response = super().to_representation(instance)
        response['product'] = PaintingSerializer(instance=instance.product).data
        return response


class HandicraftOrderSerializer(serializers.ModelSerializer):
    price = serializers.ReadOnlyField()
    total_sum = serializers.ReadOnlyField()
    order_status = serializers.ReadOnlyField()
    created = serializers.ReadOnlyField()

    class Meta:
        model = HandicraftOrder
        fields = '__all__'

    def create(self, validated_data):
        product = validated_data.get('product')
        product = Handicraft.objects.get(id=product.id)
        total_sum = validated_data['quantity'] * product.price
        price = product.price
        order = HandicraftOrder.objects.create(
            price=price,
            total_sum=total_sum,
            customer_name=validated_data['customer_name'],
            phone_number=validated_data['phone_number'],
            product=validated_data['product'],
            quantity=validated_data['quantity'],
        )
        return order

    def to_representation(self, instance):
        response = super().to_representation(instance)
        response['product'] = HandicraftSerializer(instance=instance.product).data
        return response


class CeramicOrderSerializer(serializers.ModelSerializer):
    price = serializers.ReadOnlyField()
    total_sum = serializers.ReadOnlyField()
    order_status = serializers.ReadOnlyField()
    created = serializers.ReadOnlyField()

    class Meta:
        model = CeramicOrder
        fields = '__all__'

    def create(self, validated_data):
        product = validated_data.get('product')
        product = Ceramic.objects.get(id=product.id)
        total_sum = validated_data['quantity'] * product.price
        price = product.price
        order = CeramicOrder.objects.create(
            price=price,
            total_sum=total_sum,
            customer_name=validated_data['customer_name'],
            phone_number=validated_data['phone_number'],
            product=validated_data['product'],
            quantity=validated_data['quantity'],
        )
        return order

    def to_representation(self, instance):
        response = super().to_representation(instance)
        response['product'] = CeramicSerializer(instance=instance.product).data
        return response

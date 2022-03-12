from rest_framework import serializers
from .models import OrderStatus, Order
from rest_framework.validators import UniqueValidator


class OrderStatusSerializer(serializers.ModelSerializer):
    title = serializers.ReadOnlyField(allow_null=True)

    class Meta:
        model = OrderStatus
        fields = ['id', 'title']


class OrderSerializer(serializers.ModelSerializer):
    created_date = serializers.ReadOnlyField()
    order_status = OrderStatusSerializer(default=1)

    class Meta:
        model = Order
        fields = '__all__'

    def validate(self, attrs):
        attrs = super().validate(attrs)
        total_price = attrs['total_price']
        if total_price <= 0:
            raise serializers.ValidationError(
                detail='Итоговая стоимость заказа не может иметь отрицательное значение.',
                code='negative_number_value'
            )
        return attrs

    def create(self, validated_data):
        order = Order.objects.create(
            name=validated_data['name'],
            email=validated_data['email'],
            phone=validated_data['phone'],
            country=validated_data['country'],
            region=validated_data['region'],
            city=validated_data['city'],
            comment=validated_data['comment'],
            total_price=validated_data['total_price'],
            quantity=validated_data['quantity'],
            price=validated_data['price'],
            products_id=validated_data['products_id'],
            product_name=validated_data['product_name'],
            products_category=validated_data['products_category']
        )
        return order

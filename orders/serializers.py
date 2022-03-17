from drf_writable_nested import WritableNestedModelSerializer
from rest_framework import serializers
from .models import OrderStatus, Order, OrderProduct
from products.models import Painting, Handicraft, Ceramic
from django.urls import reverse
from django.utils.safestring import mark_safe


class OrderStatusSerializer(serializers.ModelSerializer):
    title = serializers.ReadOnlyField(allow_null=True)

    class Meta:
        model = OrderStatus
        fields = ['id', 'title']


class OrderProductSerializer(WritableNestedModelSerializer):
    order = serializers.PrimaryKeyRelatedField(read_only=True)

    class Meta:
        model = OrderProduct
        fields = ['id', 'order', 'link', 'product_category', 'product_id', 'quantity', 'price']

    def create(self, validated_data):
        prod_name = ''
        if validated_data['product_category'] == 'painting':
            prod_name = f"Картина: {Painting.objects.get(id=validated_data['product_id'])}"
        elif validated_data['product_category'] == 'handicraft':
            prod_name = f"Ремесленное изделие: {Handicraft.objects.get(id=validated_data['product_id'])}"
        elif validated_data['product_category'] == 'ceramic':
            prod_name = f"Керамика: {Ceramic.objects.get(id=validated_data['product_id'])}"
        display_text = ", ".join([
            "<a href={}>{}</a>".format(
                reverse('admin:{}_{}_change'.format('products', validated_data['product_category']),
                        args=(validated_data['product_id'],)),
                prod_name)
        ])
        order_product = OrderProduct.objects.create(link=mark_safe(display_text), **validated_data)
        return order_product


class OrderSerializer(WritableNestedModelSerializer):
    order_products = OrderProductSerializer(many=True, required=False)

    class Meta:
        model = Order
        fields = ['id', 'name', 'email', 'phone', 'country', 'region', 'city', 'comment', 'created_date', 'total_price',
                  'order_status', 'order_products']

from django.contrib import admin
from django.urls import reverse
from django.utils.safestring import mark_safe
from products.models import Painting, Handicraft, Ceramic
from .models import Order, OrderStatus


class OrderStatusAdmin(admin.ModelAdmin):
    readonly_fields = ('id',)


class OrderAdmin(admin.ModelAdmin):
    list_display = ('name', 'order_status', 'products_category', 'country', 'created_date')
    list_filter = ('order_status', 'name', 'phone')

    fieldsets = (
        ('Покупатель', {
            'fields': ('name', 'email', 'phone', 'country', 'region', 'city')
        }),
        ('Товар', {
            'fields': ('get_product', 'quantity', 'price', 'total_price'),
        }),
        (None, {
            'fields': ('comment', 'created_date', 'order_status'),
        })
    )

    def get_product(self, obj):
        prod_name = ''
        if obj.products_category == 'painting':
            prod_name = f"Картина: {Painting.objects.get(id=obj.products_id)}"
        elif obj.products_category == 'handicraft':
            prod_name = f"Ремесленное изделие: {Handicraft.objects.get(id=obj.products_id)}"
        elif obj.products_category == 'ceramic':
            prod_name = f"Керамика: {Ceramic.objects.get(id=obj.products_id)}"

        display_text = ", ".join([
            "<a href={}>{}</a>".format(
                reverse('admin:{}_{}_change'.format('products', obj.products_category),
                        args=(obj.products_id,)),
                prod_name)
        ])
        if display_text:
            return mark_safe(display_text)
        return "-"
    get_product.short_description = 'Товар'

    def get_readonly_fields(self, request, obj=None):
        if obj:
            return ['name', 'email', 'phone', 'country', 'region', 'city', 'comment', 'created_date', 'total_price',
                    'quantity', 'price', 'products_id', 'product_name', 'get_product']
        else:
            return []


admin.site.register(Order, OrderAdmin)
admin.site.register(OrderStatus, OrderStatusAdmin)

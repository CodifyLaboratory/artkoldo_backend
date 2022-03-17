from django.contrib import admin
from django.utils.safestring import mark_safe
from .models import Order, OrderStatus, OrderProduct


class OrderStatusAdmin(admin.ModelAdmin):
    readonly_fields = ('id',)


class OrderProductInline(admin.TabularInline):
    model = OrderProduct
    extra = 0
    verbose_name_plural = "Товары"
    readonly_fields = ('product_link', 'quantity', 'price')
    fields = ('product_link', 'quantity', 'price')

    def product_link(self, obj):
        return mark_safe(obj.link)
    product_link.short_description = 'Товар'

    def has_add_permission(self, request, obj=None):
        return False

    def has_delete_permission(self, request, obj=None):
        return False


class OrderAdmin(admin.ModelAdmin):
    inlines = [OrderProductInline, ]
    list_display = ('name', 'id', 'order_status', 'country', 'created_date')
    list_filter = ('order_status', 'name', 'phone')

    fieldsets = (
        ('Покупатель', {
            'fields': ('name', 'email', 'phone', 'country', 'region', 'city')
        }),
        ('О заказе', {
            'fields': ('comment', 'created_date', 'order_status', 'total_price'),
        })
    )

    def get_readonly_fields(self, request, obj=None):
        if obj:
            return ['name', 'email', 'phone', 'country', 'region', 'city', 'comment', 'created_date', 'get_product',
                    'total_price']
        else:
            return []


admin.site.register(Order, OrderAdmin)
admin.site.register(OrderStatus, OrderStatusAdmin)

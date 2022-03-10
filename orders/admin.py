from django.contrib import admin
from .models import Order, OrderStatus


class OrderAdmin(admin.ModelAdmin):
    """Фильтрация в админ панели"""
    list_filter = ("name", "phone", "order_status")


admin.site.register(Order, OrderAdmin)
admin.site.register(OrderStatus)

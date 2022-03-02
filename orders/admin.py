from django.contrib import admin
from .models import PaintingOrder, HandicraftOrder, CeramicOrder


class PaintingOrderAdmin(admin.ModelAdmin):
    list_filter = ("customer_name", "phone_number", "order_status")


class HandicraftOrderAdmin(admin.ModelAdmin):
    list_filter = ("customer_name", "phone_number", "order_status")


class CeramicOrderAdmin(admin.ModelAdmin):
    list_filter = ("customer_name", "phone_number", "order_status")


admin.site.register(PaintingOrder, PaintingOrderAdmin)
admin.site.register(HandicraftOrder, HandicraftOrderAdmin)
admin.site.register(CeramicOrder, CeramicOrderAdmin)

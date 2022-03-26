from django.contrib import admin
from .models import Founder, AboutUs, Contacts, SocialMedia, Terms, ForPartners, PaymentDelivery, ContactForm, \
    ContactFormStatus, SellInfo


class InfoAdmin(admin.ModelAdmin):
    def has_add_permission(self, request):
        if self.model.objects.count() > 0:
            return False
        else:
            return True


class FounderAdmin(admin.ModelAdmin):
    def has_add_permission(self, request):
        if self.model.objects.count() == 2:
            return False
        else:
            return True


class ContactFormAdmin(admin.ModelAdmin):
    readonly_fields = ('id', 'created_at')
    list_display = ('name', 'id', 'phone_number', 'email', 'status',)
    list_filter = ('name', 'phone_number', 'email', 'status')


class ContactFormStatusAdmin(admin.ModelAdmin):
    readonly_fields = ('id',)
    list_display = ('id', 'title')


admin.site.register(Founder, FounderAdmin)
admin.site.register(AboutUs, InfoAdmin)
admin.site.register(Contacts, InfoAdmin)
admin.site.register(SocialMedia, InfoAdmin)
admin.site.register(Terms, InfoAdmin)
admin.site.register(ForPartners, InfoAdmin)
admin.site.register(PaymentDelivery, InfoAdmin)
admin.site.register(ContactForm, ContactFormAdmin)
admin.site.register(ContactFormStatus, ContactFormStatusAdmin)
admin.site.register(SellInfo, InfoAdmin)

from django.contrib import admin
from .models import Founder, AboutUs, Contacts, SocialMedia, Terms, ForPartners, PaymentDelivery


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


admin.site.register(Founder, FounderAdmin)
admin.site.register(AboutUs, InfoAdmin)
admin.site.register(Contacts, InfoAdmin)
admin.site.register(SocialMedia, InfoAdmin)
admin.site.register(Terms, InfoAdmin)
admin.site.register(ForPartners, InfoAdmin)
admin.site.register(PaymentDelivery, InfoAdmin)



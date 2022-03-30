from django.urls import path
from .views import AboutUsViewSet, ContactsViewSet, SocialMediaViewSet, ContactFormViewSet, \
    TermsViewSet, ForPartnersViewSet, PaymentDeliveryViewSet, SellInfoViwSet


urlpatterns = [
    path('about_us/', AboutUsViewSet.as_view({'get': 'list'})),
    path('contacts/', ContactsViewSet.as_view({'get': 'list'})),
    path('social_media/', SocialMediaViewSet.as_view({'get': 'list'})),
    path('contact_form/', ContactFormViewSet.as_view({'post': 'create'})),
    path('terms/', TermsViewSet.as_view({'get': 'list'})),
    path('for_partners/', ForPartnersViewSet.as_view({'get': 'list'})),
    path('payment_delivery/', PaymentDeliveryViewSet.as_view({'get': 'list'})),
    path('sell_info/', SellInfoViwSet.as_view({'get': 'list'})),
]

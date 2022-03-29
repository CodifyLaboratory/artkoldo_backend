from rest_framework import viewsets
from .models import Founder, AboutUs, Contacts, SocialMedia, ContactForm, Terms, ForPartners, PaymentDelivery, \
    SellInfo, VideoOnMainPage
from .serializers import FounderSerializer, AboutUsSerializer, ContactsSerializer, SocialMediaSerializer, \
    ContactFormSerializer, TermsSerializer, ForPartnersSerializer, PaymentDeliverySerializer, \
    SellInfoSerializer, VideoOnMainPageSerializer


class FounderViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Founder.objects.all()
    serializer_class = FounderSerializer


class AboutUsViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = AboutUs.objects.all()
    serializer_class = AboutUsSerializer


class ContactsViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Contacts.objects.all()
    serializer_class = ContactsSerializer


class SocialMediaViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = SocialMedia.objects.all()
    serializer_class = SocialMediaSerializer


class ContactFormViewSet(viewsets.ModelViewSet):
    queryset = ContactForm.objects.all()
    serializer_class = ContactFormSerializer


class TermsViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Terms.objects.all()
    serializer_class = TermsSerializer


class ForPartnersViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = ForPartners.objects.all()
    serializer_class = ForPartnersSerializer


class PaymentDeliveryViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = PaymentDelivery.objects.all()
    serializer_class = PaymentDeliverySerializer


class SellInfoViwSet(viewsets.ReadOnlyModelViewSet):
    queryset = SellInfo.objects.all()
    serializer_class = SellInfoSerializer


class VideoOnMainPageViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = VideoOnMainPage.objects.all()
    serializer_class = VideoOnMainPageSerializer

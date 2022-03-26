from rest_framework import serializers
from .models import Founder, AboutUs, Contacts, SocialMedia, ContactForm, Terms, ForPartners, PaymentDelivery, \
    ContactFormStatus, SellInfo


class FounderSerializer(serializers.ModelSerializer):

    class Meta:
        model = Founder
        fields = '__all__'


class AboutUsSerializer(serializers.ModelSerializer):

    class Meta:
        model = AboutUs
        fields = '__all__'


class ContactsSerializer(serializers.ModelSerializer):

    class Meta:
        model = Contacts
        fields = '__all__'


class SocialMediaSerializer(serializers.ModelSerializer):

    class Meta:
        model = SocialMedia
        fields = '__all__'


class ContactFormStatusSerializer(serializers.ModelSerializer):
    title = serializers.ReadOnlyField(allow_null=True)

    class Meta:
        model = ContactFormStatus
        fields = ['id', 'title']


class ContactFormSerializer(serializers.ModelSerializer):
    created_at = serializers.ReadOnlyField()

    class Meta:
        model = ContactForm
        fields = ['id', 'name', 'email', 'phone_number', 'comment', 'created_at', 'status']


class TermsSerializer(serializers.ModelSerializer):

    class Meta:
        model = Terms
        fields = '__all__'


class ForPartnersSerializer(serializers.ModelSerializer):

    class Meta:
        model = ForPartners
        fields = '__all__'


class PaymentDeliverySerializer(serializers.ModelSerializer):

    class Meta:
        model = PaymentDelivery
        fields = '__all__'


class SellInfoSerializer(serializers.ModelSerializer):

    class Meta:
        model = SellInfo
        fields = '__all__'

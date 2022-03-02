from rest_framework import viewsets
from .serializers import PaintingOrderSerializer, HandicraftOrderSerializer, CeramicOrderSerializer
from .models import PaintingOrder, HandicraftOrder, CeramicOrder


class PaintingOrderViewSet(viewsets.ModelViewSet):

    queryset = PaintingOrder.objects.all().order_by('-id')
    serializer_class = PaintingOrderSerializer


class HandicraftOrderViewSet(viewsets.ModelViewSet):

    queryset = HandicraftOrder.objects.all().order_by('-id')
    serializer_class = HandicraftOrderSerializer


class CeramicOrderViewSet(viewsets.ModelViewSet):

    queryset = CeramicOrder.objects.all().order_by('-id')
    serializer_class = CeramicOrderSerializer

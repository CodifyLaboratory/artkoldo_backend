from rest_framework import viewsets
from .serializers import OrderSerializer
from .models import Order


class OrderViewSet(viewsets.ModelViewSet):
    queryset = Order.objects.all().order_by('-created_date')
    serializer_class = OrderSerializer

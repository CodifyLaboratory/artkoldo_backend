from rest_framework import viewsets
from .serializers import OrderSerializer
from .models import Order
from django.views.decorators.csrf import csrf_exempt


@csrf_exempt
class OrderViewSet(viewsets.ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer

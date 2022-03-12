from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework import status
from .serializers import OrderSerializer
from .models import Order


class OrderViewSet(viewsets.ModelViewSet):
    queryset = Order.objects.all().order_by('-created_date')

    def create(self, request, *args, **kwargs):
        for order in request.data:
            serializer = OrderSerializer(data=order)
            if serializer.is_valid():
                serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)

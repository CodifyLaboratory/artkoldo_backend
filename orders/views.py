from rest_framework import viewsets, response, status
from .serializers import OrderSerializer
from .models import Order
from django.core.mail import send_mail


class OrderViewSet(viewsets.ModelViewSet):
    queryset = Order.objects.all().order_by('-created_date')
    serializer_class = OrderSerializer

    def perform_create(self, serializer):

        message = self.request.data['name'] + ' ' + str(self.request.data['total_price'])
        if serializer.is_valid():
            serializer.save()
        send_mail(
            'Заказ',  # Название письма
            message,  # Само письмо
            'artkoldoo2022@gmail.com',  # Емаил отправителя
            ['artkoldoo2022@gmail.com'],  # Емаил полуателя
        )
        return response.Response(serializer.data, status=status.HTTP_201_CREATED)

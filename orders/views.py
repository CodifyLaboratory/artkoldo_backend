from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework import status
from .serializers import OrderSerializer
from .models import Order
from django.core.mail import send_mail


class OrderViewSet(viewsets.ModelViewSet):
    queryset = Order.objects.all().order_by('-created_date')

    def create(self, request, *args, **kwargs):
        massage = ''
        for order in request.data:
            massage += "Продукат: " + order['product_name'] + ", цена: " + order['price'] + '\n' # формирование письма
            serializer = OrderSerializer(data=order)
            if serializer.is_valid():
                serializer.save()
        send_mail(
            'Заказ', # Название письма
            massage, # Само письмо
            'Voronov_95@list.ru', # Емаил отправителя
            ['Voronov_1993@list.ru'], # Емаил полуателя
        )
        return Response(serializer.data, status=status.HTTP_201_CREATED)

# git remote add origin https://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@github.com/CodifyLaboratory/artkoldo_backend.git

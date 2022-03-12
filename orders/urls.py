from rest_framework.routers import DefaultRouter
from django.urls import path
from .views import OrderViewSet


router = DefaultRouter()
urlpatterns = router.urls

urlpatterns += [
    path('orders/create/', OrderViewSet.as_view({'post': 'create'})),
]

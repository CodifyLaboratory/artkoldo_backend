from .views import PaintingOrderViewSet, HandicraftOrderViewSet
from rest_framework.routers import DefaultRouter


router = DefaultRouter()
router.register(r"paintings_orders", PaintingOrderViewSet, basename='paintings_order')
router.register(r"handicraft_orders", HandicraftOrderViewSet, basename='handicraft_order')
urlpatterns = router.urls

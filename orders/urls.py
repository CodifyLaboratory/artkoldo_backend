from .views import PaintingOrderViewSet, HandicraftOrderViewSet, CeramicOrderViewSet
from rest_framework.routers import DefaultRouter


router = DefaultRouter()
router.register(r"paintings_orders", PaintingOrderViewSet, basename='paintings_order')
router.register(r"handicraft_orders", HandicraftOrderViewSet, basename='handicraft_order')
router.register(r"ceramic_orders", CeramicOrderViewSet, basename='ceramic_order')
urlpatterns = router.urls

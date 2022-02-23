from rest_framework.routers import DefaultRouter

from .views import PaintingViewSet, PaintingFilterViewSet, HandicraftViewSet, CeramicViewSet

router = DefaultRouter()
router.register(r"paintings", PaintingViewSet, basename='paintings')
router.register(r"painting_filters", PaintingFilterViewSet, basename='painting_filters')
router.register(r"handicrafts", HandicraftViewSet, basename='handicrafts')
router.register(r"ceramics", CeramicViewSet, basename='ceramics')
urlpatterns = router.urls

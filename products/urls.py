from rest_framework.routers import DefaultRouter

from .views import PaintingViewSet, PaintingFilterViewSet, HandicraftViewSet, HandicraftFilterViewSet,\
    CeramicViewSet, CeramicFilterViewSet

router = DefaultRouter()
router.register(r"paintings", PaintingViewSet, basename='paintings')
router.register(r"painting_filter", PaintingFilterViewSet, basename='painting_filter')
router.register(r"handicrafts", HandicraftViewSet, basename='handicrafts')
router.register(r"handicraft_filter", HandicraftFilterViewSet, basename='handicraft_filter')
router.register(r"ceramics", CeramicViewSet, basename='ceramics')
router.register(r"ceramic_filter", CeramicFilterViewSet, basename='ceramic_filter')
urlpatterns = router.urls

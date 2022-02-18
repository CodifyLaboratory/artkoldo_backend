from rest_framework.routers import DefaultRouter

from .views import RegionViewSet, AuthorViewSet, ColorViewSet, \
    SubjectViewSet, PaintMaterialViewSet, StyleViewSet, PaintTechniqueViewSet, PaintingViewSet, \
    HandicraftTypeViewSet, HandicraftMaterialViewSet, HandicraftTechniqueViewSet, HandicraftViewSet, \
    CeramicTypeViewSet, CeramicMaterialViewSet, CeramicTechniqueViewSet, CeramicViewSet

router = DefaultRouter()
router.register(r"paintings", PaintingViewSet, basename='paintings')
router.register(r"handicrafts", HandicraftViewSet, basename='handicrafts')
router.register(r"ceramics", CeramicViewSet, basename='ceramics')
urlpatterns = router.urls

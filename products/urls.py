from django.urls import path
from .views import PaintingViewSet, PaintingFilterViewSet, HandicraftViewSet, HandicraftFilterViewSet, \
    CeramicViewSet, CeramicFilterViewSet, PaintingDetailViewSet, PaintingRecommendationsViewSet, \
    HandicraftDetailViewSet, HandicraftRecommendationsViewSet, CeramicDetailViewSet, CeramicRecommendationsViewSet, \
    RecommendedProductsViewSet, DiscountProductsViewSet


urlpatterns = [
    # Catalog and filters
    path('paintings/', PaintingViewSet.as_view({'get': 'list'})),
    path('painting_filter/', PaintingFilterViewSet.as_view({'get': 'list'})),
    path('handicrafts/', HandicraftViewSet.as_view({'get': 'list'})),
    path('handicraft_filter/', HandicraftFilterViewSet.as_view({'get': 'list'})),
    path('ceramics/', CeramicViewSet.as_view({'get': 'list'})),
    path('ceramic_filter/', CeramicFilterViewSet.as_view({'get': 'list'})),

    # Product page and recommendations
    path('paintings/<int:pk>/', PaintingDetailViewSet.as_view({'get': 'retrieve'})),
    path('painting_recommendations/<int:pk>/', PaintingRecommendationsViewSet.as_view({'get': 'list'})),
    path('handicrafts/<int:pk>/', HandicraftDetailViewSet.as_view({'get': 'list'})),
    path('handicraft_recommendations/<int:pk>/', HandicraftRecommendationsViewSet.as_view({'get': 'list'})),
    path('ceramics/<int:pk>/', CeramicDetailViewSet.as_view({'get': 'list'})),
    path('ceramic_recommendations/<int:pk>/', CeramicRecommendationsViewSet.as_view({'get': 'list'})),

    # for main page
    path('recommended_products/', RecommendedProductsViewSet.as_view({'get': 'list'})),
    path('discount_products/', DiscountProductsViewSet.as_view({'get': 'list'})),

]

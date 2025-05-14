from django.urls import path
from rest_framework.routers import DefaultRouter
# from .views import CaseViewSet, OrderViewSet, OrderItemViewSet
from rest_framework.routers import DefaultRouter
from .views import MTBBikeViewSet, RoadBikeViewSet, FrameRecommendationAPIView

router = DefaultRouter()
router.register(r'mtb', MTBBikeViewSet, basename='mtb')
router.register(r'road', RoadBikeViewSet, basename='road')
urlpatterns = [
    path('conf/frames/', FrameRecommendationAPIView.as_view(), name='frames'),
]

urlpatterns += router.urls

# urlpatterns = [

# path('mtb/', MTBBikeViewSet.as_view({'get': 'list', 'post': 'create'}), name='mtb-list'),
#
# path('road/', RoadBikeViewSet.as_view({'get': 'list', 'post': 'create'}), name='road-list'),

# Cases
# path('cases/<int:pk>/', CaseViewSet.as_view({'get': 'retrieve', 'put': 'update', 'delete': 'destroy'}),
#      name='case-detail'),
#
# # Orders
# path('orders/', OrderViewSet.as_view({'get': 'list', 'post': 'create'}), name='order-list'),
# path('orders/<int:pk>/', OrderViewSet.as_view({'get': 'retrieve', 'put': 'update', 'delete': 'destroy'}),
#      name='order-detail'),
#
# # Order Items
# path('order-items/', OrderItemViewSet.as_view({'get': 'list', 'post': 'create'}), name='orderitem-list'),
# path('order-items/<int:pk>/', OrderItemViewSet.as_view({'get': 'retrieve', 'put': 'update', 'delete': 'destroy'}),
#      name='orderitem-detail'),
# ]

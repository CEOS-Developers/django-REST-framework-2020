from django.urls import path, include
# views 에서 작성한 ViewSet 을 Router 에 연결하면 url 을 자동으로 매핑해준다. (DRF 의 router)
from rest_framework import routers
from .views import MyUserViewSet, ProductViewSet, OrderViewSet, ManufacturerViewSet, DeliveryViewSet, ReviewViewSet


router = routers.DefaultRouter()
# router.register(prefix, viewset, basename)
# The basename argument is used to specify the initial part of the view name pattern.
router.register(r'myusers', MyUserViewSet, basename='myuser-detail')
router.register(r'products', ProductViewSet, basename='product-detail')
router.register(r'orders', OrderViewSet, basename='order-detail')
router.register(r'manufacturers', ManufacturerViewSet, basename='manufacturer-detail')
router.register(r'delivery', DeliveryViewSet, basename='delivery-detail')
router.register(r'reviews', ReviewViewSet, basename='review-detail')

urlpatterns = [
    path('', include(router.urls)),
]


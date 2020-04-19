from django.urls import path, include
# views 에서 작성한 ViewSet 을 Router 에 연결하면 url 을 자동으로 매핑해준다. (DRF 의 router)
from rest_framework import routers
from .views import MyUserViewSet, ProductViewSet, OrderViewSet, ManufacturerViewSet, DeliveryViewSet, ReviewViewSet


router = routers.DefaultRouter()
router.register(r'myusers', MyUserViewSet, basename='MyUser')   # 뷰 등록 prefix = myusers, viewset = MyUserViewSet
router.register(r'products', ProductViewSet, basename='Product')
router.register(r'orders', OrderViewSet, basename='Order')
router.register(r'manufacturers', ManufacturerViewSet, basename='Manufacturer')
router.register(r'delivery', DeliveryViewSet, basename='Delivery')
router.register(r'reviews', ReviewViewSet, basename='Review')

urlpatterns = [
    path('', include(router.urls)),
]


from django.urls import path, include
# views 에서 작성한 ViewSet 을 Router 에 연결하면 url 을 자동으로 매핑해준다. (DRF 의 router)
from rest_framework import routers
from . import views


router = routers.DefaultRouter()
router.register(r'myusers', views.MyUserViewSet)   # 뷰 등록 prefix = myusers, viewset = MyUserViewSet
router.register(r'products', views.ProductViewSet)
router.register(r'orders', views.OrderViewSet)
router.register(r'manufacturers', views.ManufacturerViewSet)
router.register(r'delivery', views.DeliveryViewSet)
router.register(r'reviews', views.ReviewViewSet)

urlpatterns = [
    path('', include(router.urls)),
]


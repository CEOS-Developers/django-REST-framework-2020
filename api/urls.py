from django.urls import path, include
from . import views
from rest_framework.routers import DefaultRouter


router = DefaultRouter()
# router.register 안에 들어가는 `model_name`은 RESTful api의 url 패턴에서 리소스를 나타내주는 자리에 `model_name` 을 넣어주는 역할
router.register(r'users', views.UserViewSet)     # url 패턴 앞에 r이 들어가는 것은 무엇인가?
router.register(r'movies', views.MovieViewSet)
router.register(r'timetables', views.TimeTableViewSet)
router.register(r'reviews', views.ReviewViewSet)
router.register(r'bookings', views.BookingViewSet)

urlpatterns = [
    path('', include(router.urls))
]
# urlpatterns = router.urls

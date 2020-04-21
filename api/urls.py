from django.urls import path, include
from . import views
from rest_framework.routers import DefaultRouter


router = DefaultRouter()
router.register('users', views.UserViewSet)
router.register('movies', views.MovieViewSet)
router.register('timetables', views.TimeTableViewSet)
router.register('reviews', views.ReviewViewSet)
router.register('bookings', views.BookingViewSet)

urlpatterns = [
    path('', include(router.urls))
]
# urlpatterns = router.urls

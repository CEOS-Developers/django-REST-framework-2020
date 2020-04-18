from django.urls import path, include
from . import views
from rest_framework.routers import DefaultRouter


router = DefaultRouter()
router.register('user', views.UserViewSet)
router.register('movie', views.MovieViewSet)
router.register('timetable', views.TimeTableViewSet)
router.register('review', views.ReviewViewSet)
router.register('booking', views.BookingViewSet)

urlpatterns = [
    path('', include(router.urls))
]
# urlpatterns = router.urls

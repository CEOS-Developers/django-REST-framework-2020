from django.urls import path
from django.conf.urls import url, include
from rest_framework import routers
from .views import MovieViewSet, DirectorViewSet, GenreViewSet, CountryViewSet,WorkersViewSet

router = routers.DefaultRouter()
router.register('movies', MovieViewSet)
router.register('directors', DirectorViewSet)
router.register('genres', GenreViewSet)
router.register('countries', CountryViewSet)
router.register('workers', WorkersViewSet)

urlpatterns = [
    url(r'^', include(router.urls)),
]

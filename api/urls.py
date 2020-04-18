from django.urls import path
from django.conf.urls import url, include
from rest_framework import routers
from .views import MovieViewSet, DirectorViewSet, GenreViewSet, CountryViewSet

router = routers.DefaultRouter()
router.register('movie', MovieViewSet)
router.register('director', DirectorViewSet)
router.register('genre', GenreViewSet)
router.register('country', CountryViewSet)

urlpatterns = [
    url(r'^', include(router.urls)),
]

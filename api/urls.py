from django.urls import path
from django.conf.urls import url, include
from rest_framework import routers
from .views import MovieViewSet, DirectorViewSet, GenreViewSet, CountryViewSet,WorkersViewSet,MemberViewSet

router = routers.DefaultRouter()
router.register('movies', MovieViewSet)
router.register('directors', DirectorViewSet)
router.register('genres', GenreViewSet)
router.register('countries', CountryViewSet)
router.register('workers', WorkersViewSet)
router.register('members', MemberViewSet)

urlpatterns = [
    url(r'^', include(router.urls)),
]

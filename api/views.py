from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from .models import Movie, Director, Genre, Country, Workers, Member
from .serializers import *
from datetime import date
from .filters import *
from .permissions import *


class MovieViewSet(viewsets.ModelViewSet):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer
    permission_classes = (IsAuthenticatedOrReadOnly,)

    # url: /movies/long-movies 상영시간이 120분보다 긴 영화들 조회
    @action(methods=['get'], detail=False, url_path='long-movies', url_name='long-movies')
    def long_movies(self, request):
        mv = self.get_queryset().filter(running_time__gte=120)
        serializer = self.get_serializer(mv, many=True)
        return Response(serializer.data)

    # url : /movies/{pk}/release-today 개봉일을 오늘 날짜로 바꿔줌
    @action(methods=['post'], detail=True, url_path='release-today', url_name='release-today')
    def release_today(self, request, pk):
        today = date.today()
        instance = self.get_object()
        instance.release_date = today
        instance.save()
        serializer = self.get_serializer(instance)
        return Response(serializer.data)


class DirectorViewSet(viewsets.ModelViewSet):
    queryset = Director.objects.all()
    serializer_class = DirectorSerializer
    permission_classes = (IsAuthenticatedOrReadOnly,)


class GenreViewSet(viewsets.ModelViewSet):
    queryset = Genre.objects.all()
    serializer_class = GenreSerializer
    permission_classes = (IsAuthenticatedOrReadOnly,)


class CountryViewSet(viewsets.ModelViewSet):
    queryset = Country.objects.all()
    serializer_class = CountrySerializer
    permission_classes = (IsAuthenticatedOrReadOnly,)


class WorkersViewSet(viewsets.ModelViewSet):
    queryset = Workers.objects.all()
    serializer_class = WorkersSerializer
    filter_backends = [DjangoFilterBackend]
    filter_class = WorkersFilter
    permission_classes = (IsSuperUser,)


class MemberViewSet(viewsets.ModelViewSet):
    queryset = Member.objects.all()
    serializer_class = MemberSerializer
    permission_classes = (IsAdminUser,)
# generics
# class MovieListGenericAPIView(generics.ListCreateAPIView):
#     queryset = Movie.objects.all()
#     serializer_class = MovieSerializer
#
#
# class MovieDetailGenericAPIView(generics.RetrieveUpdateDestroyAPIView):
#     queryset = Movie.objects.all()
#     serializer_class = MovieSerializer
#

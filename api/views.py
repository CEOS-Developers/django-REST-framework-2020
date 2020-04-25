from django.shortcuts import render
from rest_framework import viewsets
from rest_framework import generics
from rest_framework.decorators import action
from rest_framework.response import Response
from .models import Movie, Director, Genre, Country
from .serializers import MovieSerializer, DirectorSerializer, GenreSerializer, CountrySerializer
from datetime import date


class MovieViewSet(viewsets.ModelViewSet):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer

    # url: /movies/long_movies 상영시간이 120분보다 긴 영화들 조회
    @action(methods=['get'], detail=False, url_path='long-movies', url_name='long_movies')
    def long_movies(self, request):
        mv = self.get_queryset()
        long_mv = []
        for movie in mv:
            if movie.running_time > 120:
                long_mv.append(movie)

        serializer = self.get_serializer(long_mv, many=True)
        return Response(serializer.data)

    # url : /movies/{pk}/release-today 개봉일을 오늘 날짜로 바꿔줌
    @action(methods=['post'], detail=True, url_path='release-today', url_name='release_today')
    def release_today(self, request, pk):
        today = date.today()
        instance = self.get_object()
        instance.release_date = today
        serializer = self.get_serializer(instance)
        return Response(serializer.data)


class DirectorViewSet(viewsets.ModelViewSet):
    queryset = Director.objects.all()
    serializer_class = DirectorSerializer


class GenreViewSet(viewsets.ModelViewSet):
    queryset = Genre.objects.all()
    serializer_class = GenreSerializer


class CountryViewSet(viewsets.ModelViewSet):
    queryset = Country.objects.all()
    serializer_class = CountrySerializer

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

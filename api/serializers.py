from django.contrib.auth.models import User, Group  # 기존 장고 모델
from rest_framework import serializers
from .models import Movie, Director, Genre, Country


class MovieSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = ('title', 'director', 'release_date', 'running_time', 'country', 'genre')


class DirectorSerializer(serializers.ModelSerializer):
    movies = MovieSerializer(many=True)

    class Meta:
        model = Director
        fields = ('name', 'movies')


class GenreSerializer(serializers.ModelSerializer):
    movies = MovieSerializer(many=True)

    class Meta:
        model = Genre
        fields = ('name', 'movies')


class CountrySerializer(serializers.ModelSerializer):
    movies = MovieSerializer(many=True)

    class Meta:
        model = Country
        fields = ('name', 'movies')

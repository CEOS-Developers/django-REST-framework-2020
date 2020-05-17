from django.contrib.auth.models import User, Group  # 기존 장고 모델
from rest_framework import serializers
from .models import Movie, Director, Genre, Country, Workers
import datetime


class MovieSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = ('id', 'title', 'director', 'release_date', 'running_time', 'country', 'genre')


class DirectorSerializer(serializers.ModelSerializer):
    movies = MovieSerializer(many=True)

    class Meta:
        model = Director
        fields = ('id', 'name', 'movies')


class GenreSerializer(serializers.ModelSerializer):
    movies = MovieSerializer(many=True)

    class Meta:
        model = Genre
        fields = ('id', 'name', 'movies')


class CountrySerializer(serializers.ModelSerializer):
    movies = MovieSerializer(many=True)

    class Meta:
        model = Country
        fields = ('id', 'name', 'movies')


class WorkersSerializer(serializers.ModelSerializer):
    days_since_joined = serializers.SerializerMethodField()

    def get_days_since_joined(self, obj):
        return (datetime.date.today() - obj.join_date).days

    class Meta:
        model = Workers
        fields = '__all__'

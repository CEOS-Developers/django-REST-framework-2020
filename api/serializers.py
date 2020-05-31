from django.utils.timezone import now
from rest_framework import serializers
from .models import User, Movie, TimeTable, Review, Booking, Genre


class UserSerializer(serializers.ModelSerializer):
    days_since_joined = serializers.SerializerMethodField()

    class Meta:
        model = User
        exclude = ('first_name', 'last_name', 'groups')

    def get_days_since_joined(self, obj):
        return (now() - obj.date_joined).days


class MovieSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = '__all__'


class TimeTableSerializer(serializers.ModelSerializer):
    movies = MovieSerializer(many=True)

    class Meta:
        model = TimeTable
        fields = ('id', 'name', 'movies', 'start_time', 'end_time')


class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = '__all__'


class BookingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Booking
        fields = '__all__'


class GenreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Genre
        fields = ('name', 'movie')

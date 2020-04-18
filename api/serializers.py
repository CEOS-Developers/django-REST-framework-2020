from rest_framework import serializers
from .models import User, Movie, TimeTable, Review, Booking


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        exclude = ('first_name', 'last_name', 'groups')


class MovieSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = '__all__'


class TimeTableSerializer(serializers.ModelSerializer):
    class Meta:
        model = TimeTable
        fields = '__all__'


class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = '__all__'


class BookingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Booking
        fields = '__all__'

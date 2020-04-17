from django.contrib.auth.models import User, Group  # 기존 장고 모델
from rest_framework import serializers
from api.models import *


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User  # 사용할 모델
        fields = ['url', 'tel', 'email', 'groups']  # 사용할 모델의 필드


class BranchSerializer(serializers.ModelSerializer):
    class Meta:
        model = Branch
        fields = ['id', 'name', 'location']


class ScreenSerializer(serializers.ModelSerializer):
    class Meta:
        model = Screen
        fields = '__all__'


class MovieSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = '__all__'


class ScheduleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Schedule
        fields = '__all__'

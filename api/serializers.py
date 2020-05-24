from rest_framework import serializers
from api.models import User, Major, Student, Professor, Course, Basket, Registration


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['user_id', 'name', 'password']
        extra_kwargs = {'password':{'write_only':True},}


class MajorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Major
        fields = '__all__'


class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = ['std_id', 'credits_available', 'current_credits']


class ProfessorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Professor
        fields = ['prof_name']


class CourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = '__all__'


class BasketSerializer(serializers.ModelSerializer):
    class Meta:
        model = Basket
        fields = '__all__'


class RegSerializer(serializers.ModelSerializer):
    course = CourseSerializer(many=True, read_only=True)

    class Meta:
        model = Registration
        fields = '__all__'

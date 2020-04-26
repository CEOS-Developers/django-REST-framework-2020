from rest_framework import serializers
from api.models import Major, Student, Professor, Course, Registration


class MajorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Major
        fields = '__all__'


class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = ['std_id', 'credits_available']


class ProfessorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Professor
        fields = ['prof_name']


class CourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = '__all__'


class RegSerializer(serializers.ModelSerializer):
    class Meta:
        model = Registration
        fields = '__all__'
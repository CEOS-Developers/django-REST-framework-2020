from api.serializers import *
from rest_framework import generics


class MajorView(generics.ListCreateAPIView):
    queryset = Major.objects.all()
    serializer_class = MajorSerializer


class StudentView(generics.ListCreateAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer


class ProfessorView(generics.ListCreateAPIView):
    queryset = Professor.objects.all()
    serializer_class = ProfessorSerializer


class CourseView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer



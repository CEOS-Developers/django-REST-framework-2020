from api.serializers import *
from rest_framework import generics


class MajorList(generics.ListAPIView):
    queryset = Major.objects.all()
    serializer_class = MajorSerializer


class MajorDetail(generics.RetrieveAPIView):
    queryset = Major.objects.all()
    serializer_class = MajorSerializer


class StudentList(generics.ListAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer


class StudentDetail(generics.RetrieveAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer


class ProfessorList(generics.ListAPIView):
    queryset = Professor.objects.all()
    serializer_class = ProfessorSerializer


class ProfessorDetail(generics.RetrieveAPIView):
    queryset = Professor.objects.all()
    serializer_class = ProfessorSerializer


class CourseList(generics.ListAPIView):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer


class CourseDetail(generics.RetrieveAPIView):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer



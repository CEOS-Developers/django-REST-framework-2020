from rest_framework.response import Response
from api.serializers import *
from rest_framework import viewsets, status, permissions
from rest_framework.decorators import action
from django_filters.rest_framework import DjangoFilterBackend
from django_filters.rest_framework import FilterSet, filters
from api.filter import *


SAFE_METHODS = {'GET', 'OPTIONS', 'HEAD'}


class IsSuperUserOrReadOnly(permissions.BasePermission):
    def has_permission(self, request, view):
        if request.method in permissions.SAFE_METHODS:
            return True
        return request.user.is_superuser


class IsAuthenticated(permissions.BasePermission):
    def has_permission(self, request, view):
        return request.user and request.user.is_authenticated


class UserView(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = (IsAuthenticated,)


class MajorView(viewsets.ModelViewSet):
    queryset = Major.objects.all()
    serializer_class = MajorSerializer


class StudentView(viewsets.ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    permission_classes = (IsAuthenticated,)


class ProfessorView(viewsets.ModelViewSet):
    queryset = Professor.objects.all()
    serializer_class = ProfessorSerializer


class CourseView(viewsets.ModelViewSet):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer
    permission_classes = (IsSuperUserOrReadOnly,)
    filter_backends = [DjangoFilterBackend]
    filterset_class1 = WeekdayFilter
    filterset_class2 = CreditFilter

    @action(methods=['get'], detail=False, url_path='course_wed', url_name='course-wed')  # 수요일에 하는 강의 조회
    def course_wed(self, request):
        course_wed = self.get_queryset().filter(weekday='Wed')
        serializer = self.get_serializer(course_wed, many=True)
        return Response(serializer.data)

    @action(methods=['patch'], detail=False, url_path='change_weekday', url_name='change-weekday')
    def change_weekday(self, request, pk):
        inst = self.get_object()
        inst.weekday = "weekday"
        inst.save()
        serializer = self.get_serializer(inst)
        return Response(serializer.data)


class BasketView(viewsets.ModelViewSet):
    queryset = Basket.objects.all()
    serializer_class = BasketSerializer
    permission_classes = (IsAuthenticated,)


class RegView(viewsets.ModelViewSet):
    queryset = Registration.objects.all()
    serializer_class = RegSerializer
    permission_classes = (IsAuthenticated,)

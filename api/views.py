from django.contrib.auth import authenticate
from rest_framework import permissions, viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from api.serializers import *
from django_filters.rest_framework import DjangoFilterBackend
from api.filter import *


class IsAdmin(permissions.BasePermission):
    def has_permission(self, request, views):
        if request.user.is_admin:
            return True
        return False


class AuthenticatedReadOnly(permissions.BasePermission):
    def has_permission(self, request, view):
        if request.user.is_authenticated:
            if request.method in permissions.SAFE_METHODS:
                return True
            else:
                return False
        return False


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = (IsAdmin,)


class BranchViewSet(viewsets.ModelViewSet):
    queryset = Branch.objects.all()
    serializer_class = BranchSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_class = BranchFilter
    permission_classes = (AuthenticatedReadOnly,)


class ScreenViewSet(viewsets.ModelViewSet):
    queryset = Screen.objects.all()
    serializer_class = ScreenSerializer
    permission_classes = (AuthenticatedReadOnly,)


class MovieViewSet(viewsets.ModelViewSet):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_class = MovieFilter
    permission_classes = (AuthenticatedReadOnly,)


class ScheduleViewSet(viewsets.ModelViewSet):
    queryset = Schedule.objects.all()
    serializer_class = ScheduleSerializer
    permission_classes = (AuthenticatedReadOnly,)

    @action(detail=True, methods=['get'], url_path='get-running-time', url_name='get_running_time')
    def get_running_time(self, request, pk):
        serializer = self.get_serializer(self.get_object())
        finish = datetime.strptime(serializer.data['finish_time'], '%Y-%m-%dT%H:%M:%S%z')
        start = datetime.strptime(serializer.data['start_time'], '%Y-%m-%dT%H:%M:%S%z')
        running_time: int = ((finish - start).seconds / 60)
        return Response("running time : " + str(running_time) + "분")

from django.shortcuts import render
from rest_framework import permissions, viewsets, status
from rest_framework.decorators import action
from rest_framework.exceptions import PermissionDenied
from rest_framework.response import Response
from api.serializers import *
from datetime import datetime
from django_filters.rest_framework import DjangoFilterBackend
from api.models import *
from api.filter import *

SAFE_METHODS = ('GET', 'HEAD', 'OPTIONS')


class IsAuthenticatedOnly(permissions.BasePermission):
    def has_permission(self, request, view):
        if request.method in permissions.SAFE_METHODS:
            return True
        return request.user.is_authenticated


class IsNotAnonymous(permissions.BasePermission):
    def has_permission(self, request, view):
        if request.user.is_anonymous:
            return False


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = (IsNotAnonymous,)


class BranchViewSet(viewsets.ModelViewSet):
    queryset = Branch.objects.all()
    serializer_class = BranchSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_class = BranchFilter


class ScreenViewSet(viewsets.ModelViewSet):
    queryset = Screen.objects.all()
    serializer_class = ScreenSerializer


class MovieViewSet(viewsets.ModelViewSet):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_class = MovieFilter
    permission_classes = (IsAuthenticatedOnly,)


class ScheduleViewSet(viewsets.ModelViewSet):
    queryset = Schedule.objects.all()
    serializer_class = ScheduleSerializer
    permission_classes = (IsAuthenticatedOnly, )

    @action(detail=True, methods=['get'], url_path='get-running-time', url_name='get_running_time')
    def get_running_time(self, request, pk):
        serializer = self.get_serializer(self.get_object())
        finish = datetime.strptime(serializer.data['finish_time'], '%Y-%m-%dT%H:%M:%S%z')
        start = datetime.strptime(serializer.data['start_time'], '%Y-%m-%dT%H:%M:%S%z')
        running_time = (int)((finish - start).seconds / 60)
        return Response("running time : " + str(running_time) + "분")

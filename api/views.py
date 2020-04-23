from rest_framework import permissions, viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response
from api.serializers import *
from datetime import datetime

SAFE_METHODS = ('GET', 'HEAD', 'OPTIONS')


class IsAdminOnly(permissions.BasePermission):
    def has_permission(self, request, view):
        return request.user.is_authenticated

    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True
        return request.user.is_admin


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsAdminOnly, ]


class BranchViewSet(viewsets.ModelViewSet):
    queryset = Branch.objects.all()
    serializer_class = BranchSerializer
    permission_classes = [IsAdminOnly,]


class ScreenViewSet(viewsets.ModelViewSet):
    queryset = Screen.objects.all()
    serializer_class = ScreenSerializer
    permission_classes = [IsAdminOnly, ]


class MovieViewSet(viewsets.ModelViewSet):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer
    permission_classes = [IsAdminOnly, ]


class ScheduleViewSet(viewsets.ModelViewSet):
    queryset = Schedule.objects.all()
    serializer_class = ScheduleSerializer
    permission_classes = [IsAdminOnly, ]

    @action(detail=True, methods=['get'], url_path='get-running-time', url_name='get_running_time')
    def get_running_time(self, request, pk):
        schedule = self.get_object()
        serializer = ScheduleSerializer(schedule)
        finish = datetime.strptime(serializer.data['finish_time'], '%Y-%m-%dT%H:%M:%S%z')
        start = datetime.strptime(serializer.data['start_time'], '%Y-%m-%dT%H:%M:%S%z')
        running_time = (int) ((finish - start).seconds/60)
        return Response("running time : "+str(running_time)+"분")




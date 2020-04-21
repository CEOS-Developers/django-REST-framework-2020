from rest_framework import permissions, generics, status
from api.serializers import *
from rest_framework import permissions

SAFE_METHODS = ('GET', 'HEAD', 'OPTIONS')


class IsSuperuserOnly(permissions.BasePermission):
    def has_permission(self, request, view):
        return request.user.is_authenticated

    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True
        return request.user.is_superuser


class UserList(generics.ListCreateAPIView):
    permission_classes = [IsSuperuserOnly, ]
    queryset = User.objects.all()
    serializer_class = UserSerializer


class UserDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [IsSuperuserOnly, ]
    queryset = User.objects.all()
    serializer_class = UserSerializer


class BranchList(generics.ListCreateAPIView):
    permission_classes = [IsSuperuserOnly, ]
    queryset = Branch.objects.all()
    serializer_class = BranchSerializer


class BranchDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [IsSuperuserOnly, ]
    queryset = Branch.objects.all()
    serializer_class = BranchSerializer


class ScreenList(generics.ListCreateAPIView):
    permission_classes = [IsSuperuserOnly, ]
    queryset = Screen.objects.all()
    serializer_class = ScreenSerializer


class MovieList(generics.ListCreateAPIView):
    permission_classes = [IsSuperuserOnly, ]
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer


class MovieDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [IsSuperuserOnly, ]
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer


class ScheduleListCreate(generics.ListCreateAPIView):
    permission_classes = [IsSuperuserOnly, ]
    queryset = Schedule.objects.all()
    serializer_class = ScheduleSerializer


class ScheduleDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [IsSuperuserOnly, ]
    queryset = Schedule.objects.all()
    serializer_class = ScheduleSerializer


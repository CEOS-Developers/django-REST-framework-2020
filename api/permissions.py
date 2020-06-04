from rest_framework import permissions

SAFE_METHODS = ('GET', 'HEAD', 'OPTIONS')


# 유저가 존재하고 스태프일 경우에 허가
class IsAdminUser(permissions.BasePermission):
    def has_permission(self, request, view):
        return bool(request.user and request.user.is_staff)


# super user only
class IsSuperUser(permissions.BasePermission):
    def has_permission(self, request, view):
        return bool(request.user and request.user.is_superuser)


# 안전한 request method 이거나 유저가 존재하고 로그인 되어 있을 경우에 허가
class IsAuthenticatedOrReadOnly(permissions.BasePermission):
    def has_permission(self, request, view):
        return bool(
            request.method in SAFE_METHODS or
            request.user and
            request.user.is_authenticated
        )

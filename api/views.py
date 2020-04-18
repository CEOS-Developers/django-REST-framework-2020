"""
DRF 는 자주 사용하는 공통적인 view 로직을 그룹화 한 viewsets 를 제공한다.
여러 개의 view 를 작성하지 않고, 공통적인 행위들을 ViewSet 에 하나로 그룹화하여 간결하게 사용할 수 있다.
"""
from rest_framework import viewsets
from .serializers import MyUserSerializer
from .models import MyUser


class MyUserViewSet(viewsets.ModelViewSet):
    queryset = MyUser.objects.all()
    serializer_class = MyUserSerializer



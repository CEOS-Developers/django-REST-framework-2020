"""
DRF 는 자주 사용하는 공통적인 view 로직을 그룹화 한 viewsets 를 제공한다.
여러 개의 view 를 작성하지 않고, 공통적인 행위들을 ViewSet 에 하나로 그룹화하여 간결하게 사용할 수 있다.
"""
from django.db.models import QuerySet
from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from .models import MyUser, Product, Order, Manufacturer, Delivery, Review
from .serializers import MyUserSerializer, ProductSerializer, OrderSerializer, \
    ManufacturerSerializer, DeliverySerializer, ReviewSerializer


class MyUserViewSet(viewsets.ModelViewSet):
    serializer_class = MyUserSerializer
    queryset = MyUser.objects.all().order_by("-date_joined")   # list 형식


class ProductViewSet(viewsets.ModelViewSet):
    serializer_class = ProductSerializer
    queryset = Product.objects.all().order_by("-supply_date")


class OrderViewSet(viewsets.ModelViewSet):
    serializer_class = OrderSerializer
    queryset = Order.objects.all().order_by("-date_ordered")


class ManufacturerViewSet(viewsets.ModelViewSet):
    serializer_class = ManufacturerSerializer
    queryset = Manufacturer.objects.all().order_by("-manu_num")


class DeliveryViewSet(viewsets.ModelViewSet):
    serializer_class = DeliverySerializer
    queryset = Delivery.objects.all().order_by("-transport")

    # deliveries/completed/   완료된 배송 조회
    @action(methods=['get'], detail=False, url_path='completed', url_name='completed')
    def completed(self, request):
        deliveries_started = self.get_queryset().filter(state='completed')
        serializer = self.get_serializer(deliveries_started, many=True)
        return Response(serializer.data)

class ReviewViewSet(viewsets.ModelViewSet):
    serializer_class = ReviewSerializer
    queryset = Review.objects.all().order_by("-review_num")

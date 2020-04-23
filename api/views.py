"""
DRF 는 자주 사용하는 공통적인 view 로직을 그룹화 한 viewsets 를 제공한다.
여러 개의 view 를 작성하지 않고, 공통적인 행위들을 ViewSet 에 하나로 그룹화하여 간결하게 사용할 수 있다.
"""
from django.shortcuts import render
from rest_framework import viewsets
from .models import MyUser, Product, Order, Manufacturer, Delivery, Review
from .serializers import MyUserSerializer, ProductSerializer, OrderSerializer, \
    ManufacturerSerializer, DeliverySerializer, ReviewSerializer


class MyUserViewSet(viewsets.ModelViewSet):
    # queryset : how do I get all the information from the database
    # 가독성을 위해 가독성을 위해 get_queryset 을 queryset 으로 변경
    """
    def get_queryset(self):
        return MyUser.objects.all().order_by("-date_joined")
    """
    queryset = MyUser.objects.all().order_by("-date_joined")
    serializer_class = MyUserSerializer

    def perform_create(self, serializer):
        serializer.save()


class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all().order_by("-supply_date")
    serializer_class = ProductSerializer

    def perform_create(self, serializer):
        serializer.save()


class OrderViewSet(viewsets.ModelViewSet):
    queryset = Order.objects.all().order_by("-date_ordered")
    serializer_class = OrderSerializer

    def perform_create(self, serializer):
        serializer.save()


class ManufacturerViewSet(viewsets.ModelViewSet):
    queryset = Manufacturer.objects.all().order_by("-manu_num")
    serializer_class = ManufacturerSerializer

    def perform_create(self, serializer):
        serializer.save()


class DeliveryViewSet(viewsets.ModelViewSet):
    queryset = Delivery.objects.all().order_by("-transport")
    serializer_class = DeliverySerializer

    def perform_create(self, serializer):
        serializer.save()


class ReviewViewSet(viewsets.ModelViewSet):
    queryset = Review.objects.all().order_by("-review_num")
    serializer_class = ReviewSerializer

    def perform_create(self, serializer):
        serializer.save()


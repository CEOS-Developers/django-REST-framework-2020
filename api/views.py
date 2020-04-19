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
    # queryset = MyUser.objects.all()
    serializer_class = MyUserSerializer

    def get_queryset(self):
        return MyUser.objects.all().order_by("-date_joined")

    def perform_create(self, serializer):
        serializer.save()


class ProductViewSet(viewsets.ModelViewSet):
    serializer_class = ProductSerializer

    def get_queryset(self):
        return Product.objects.all().order_by("-supply_date")

    def perform_create(self, serializer):
        serializer.save()


class OrderViewSet(viewsets.ModelViewSet):
    serializer_class = OrderSerializer

    def get_queryset(self):
        return Order.objects.all().order_by("-date_ordered")

    def perform_create(self, serializer):
        serializer.save()


class ManufacturerViewSet(viewsets.ModelViewSet):
    serializer_class = ManufacturerSerializer
    # queryset = Manufacturer.objects.all()

    def get_queryset(self):
        return Manufacturer.objects.all().order_by("-manu_num")

    def perform_create(self, serializer):
        serializer.save()


class DeliveryViewSet(viewsets.ModelViewSet):
    serializer_class = DeliverySerializer

    def get_queryset(self):
        return Delivery.objects.all().order_by("-transport")

    def perform_create(self, serializer):
        serializer.save()


class ReviewViewSet(viewsets.ModelViewSet):
    serializer_class = ReviewSerializer

    def get_queryset(self):
        return Review.objects.all().order_by("-review_num")

    def perform_create(self, serializer):
        serializer.save()


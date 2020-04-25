"""
DRF 는 자주 사용하는 공통적인 view 로직을 그룹화 한 viewsets 를 제공한다.
여러 개의 view 를 작성하지 않고, 공통적인 행위들을 ViewSet 에 하나로 그룹화하여 간결하게 사용할 수 있다.
"""
from django.db.models import QuerySet
from rest_framework import viewsets
from rest_framework.decorators import action
from .models import MyUser, Product, Order, Manufacturer, Delivery, Review
from .serializers import MyUserSerializer, ProductSerializer, OrderSerializer, \
    ManufacturerSerializer, DeliverySerializer, ReviewSerializer


class MyUserViewSet(viewsets.ModelViewSet):
    serializer_class = MyUserSerializer

    # queryset = MyUser.objects.all().order_by("-date_joined")
    """
    def get_queryset(self):
        return MyUser.objects.all().order_by("-date_joined")
        
    def perform_create(self, serializer):
        serializer.save()
    """
    @property
    def queryset(self):
        queryset: QuerySet[MyUser]   # type annotation
        queryset = MyUser.objects.all().order_by("-date_joined")
        return queryset

    def perform_create(self, serializer):
        serializer.save()


class ProductViewSet(viewsets.ModelViewSet):
    serializer_class = ProductSerializer

    @property
    def queryset(self):
        queryset: QuerySet[Product]
        queryset = Product.objects.all().order_by("-supply_date")
        return queryset

    def perform_create(self, serializer):
        serializer.save()


class OrderViewSet(viewsets.ModelViewSet):
    serializer_class = OrderSerializer

    @property
    def queryset(self):
        queryset: QuerySet[Order]
        queryset = Order.objects.all().order_by("-date_ordered")
        return queryset

    def perform_create(self, serializer):
        serializer.save()


class ManufacturerViewSet(viewsets.ModelViewSet):
    serializer_class = ManufacturerSerializer

    @property
    def queryset(self):
        queryset: QuerySet[Manufacturer]
        queryset = Manufacturer.objects.all().order_by("-manu_num")
        return queryset

    def perform_create(self, serializer):
        serializer.save()


class DeliveryViewSet(viewsets.ModelViewSet):
    serializer_class = DeliverySerializer

    @property
    def queryset(self):
        queryset: QuerySet[Delivery]
        queryset = Delivery.objects.all().order_by("-transport")
        return queryset

    def perform_create(self, serializer):
        serializer.save()


class ReviewViewSet(viewsets.ModelViewSet):
    serializer_class = ReviewSerializer

    @property
    def queryset(self):
        queryset: QuerySet[Review]
        queryset = Review.objects.all().order_by("-review_num")
        return queryset

    def perform_create(self, serializer):
        serializer.save()


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
from django.utils import timezone
import datetime


class MyUserViewSet(viewsets.ModelViewSet):
    serializer_class = MyUserSerializer
    queryset = MyUser.objects.all().order_by("-date_joined")   # list 형식

    # myusers/{pk}/set-address/   주소 변경
    @action(methods=['patch'], detail=True, url_path='set-address', url_name='set_address')
    def set_address(self, request, pk):
        instance = self.get_object()
        instance.address = "new_address"
        instance.save()
        serializer = self.get_serializer(instance)
        return Response(serializer.data)


class ProductViewSet(viewsets.ModelViewSet):
    serializer_class = ProductSerializer
    queryset = Product.objects.all().order_by("-supply_date")

    # products/many-inventory/   재고량 100개 이상인 상품 조회 (발주 조절)
    @action(methods=['get'], detail=False, url_path='many-inventory', url_name='many_inventory')
    def many_inventory(self, request):
        inventory = self.get_queryset().filter(inventory__gte=100)
        serializer = self.get_serializer(inventory, many=True)
        return Response(serializer.data)


class OrderViewSet(viewsets.ModelViewSet):
    serializer_class = OrderSerializer
    queryset = Order.objects.all().order_by("-date_ordered")

    # orders/today/   오늘 주문 들어온 상품 조회
    @action(methods=['get'], detail=False, url_path='today', url_name='today')
    def today(self, request):
        today_min = datetime.datetime.combine(timezone.now().date(), datetime.time.min)
        today_max = datetime.datetime.combine(timezone.now().date(), datetime.time.max)

        orders_today = self.get_queryset().filter(date_ordered__range=(today_min, today_max))
        serializer = self.get_serializer(orders_today, many=True)
        return Response(serializer.data)


class ManufacturerViewSet(viewsets.ModelViewSet):
    serializer_class = ManufacturerSerializer
    queryset = Manufacturer.objects.all().order_by("-manu_num")

    # manufactures/address-busan/   부산에 위치한 제조업체 조회
    @action(methods=['get'], detail=False, url_path='address-busan', url_name='address_busan')
    def address_busan(self, request):
        manu_busan = self.get_queryset().filter(address__contains='busan')
        serializer = self.get_serializer(manu_busan, many=True)
        return Response(serializer.data)


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

    # reviews/image/   사진 있는 리뷰만 조회
    @action(methods=['get'], detail=False, url_path='image', url_name='image')
    def image(self, request):
        reviews = self.get_queryset()
        reviews_images = []
        for review in reviews:
            if review.image:
                reviews_images.append(review)
            serializer = self.get_serializer(reviews_images, many=True)
            return Response(serializer.data)
        return Response('No review having images')


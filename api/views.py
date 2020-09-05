# from django.db.models import QuerySet
from django_filters import rest_framework as filters
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import permissions
from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from .models import MyUser, Product, Order, Manufacturer, Delivery, Review
from .serializers import MyUserSerializer, ProductSerializer, OrderSerializer, \
    ManufacturerSerializer, DeliverySerializer, ReviewSerializer
from django.utils import timezone
import datetime


########## Filter ##########
class ProductFilter(filters.FilterSet):
    # products/?name=pencil
    name = filters.CharFilter(field_name='pro_name')
    # products/?is_soldout=true
    is_soldout = filters.BooleanFilter(method='filter_is_soldout')
    # products/?than_hundred=true
    than_hundred = filters.BooleanFilter(method='filter_than_hundred')

    class Meta:
        model = Product
        fields = ['name', 'is_soldout', 'than_hundred']   # 이 fields 는 어떤 역할인지 궁금합니다.

    # 재고량(inventory)이 0인 객체 찾기 (목적 : 품절 확인)
    def filter_is_soldout(self, queryset, name, value):
        filtered_queryset = queryset.filter(inventory__lte=0)
        return filtered_queryset

    # 재고량(inventory)이 100개 이상인 객체 찾기 (목적 : 발주 조절)
    # ProductViewSet 의 @action 기능과 겹친다.
    def filter_than_hundred(self, queryset, name, value):
        filtered_queryset = queryset.filter(inventory__gte=100)
        return filtered_queryset


class OrderFilter(filters.FilterSet):
    # orders/?destination=Jeju
    ## orders/?destination=Jeju&is_message=True (x 보류)
    destination = filters.CharFilter(method='filter_jeju_destination')
    # is_message = filters.BooleanFilter(method='filter_is_message')

    class Meta:
        model = Order
        fields = ['destination']

    # 제주(, 산간) 배송 목적지(destination) 주문 찾기 (목적 : 배송료 추가)
    def filter_jeju_destination(self, queryset, name, value):
        filtered_queryset = queryset.filter(destination__icontains='Jeju')
        return filtered_queryset

    # 주문 요청사항(message) 있는지 찾기 (목적 : 배송자에게 전달)
    # models.py 에서 Order 테이블의 message가 null=True가 아닌 blank=True로 모델링 되어있어, 나중으로 보류
    '''
    def filter_is_message(self, queryset, name, value):
        filtered_queryset = queryset.filter(message=True)
        return filtered_queryset
    '''


########## ViewSet ##########
class MyUserViewSet(viewsets.ModelViewSet):
    serializer_class = MyUserSerializer
    queryset = MyUser.objects.all().order_by("-date_joined")   # list 형식
    permission_classes = (permissions.IsAuthenticated,)

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
    permission_classes = (permissions.AllowAny,)

    # products/many-inventory/   재고량 100개 이상인 상품 조회 (목적 : 발주 조절)
    @action(methods=['get'], detail=False, url_path='many-inventory', url_name='many_inventory')
    def many_inventory(self, request):
        inventory = self.get_queryset().filter(inventory__gte=100)
        serializer = self.get_serializer(inventory, many=True)
        return Response(serializer.data)

    filter_backends = [DjangoFilterBackend]
    filter_class = ProductFilter


class OrderViewSet(viewsets.ModelViewSet):
    serializer_class = OrderSerializer
    queryset = Order.objects.all().order_by("-date_ordered")
    permission_classes = (permissions.AllowAny,)

    # orders/today/   오늘 주문 들어온 상품 조회
    @action(methods=['get'], detail=False, url_path='today', url_name='today')
    def today(self, request):
        today_min = datetime.datetime.combine(timezone.now().date(), datetime.time.min)
        today_max = datetime.datetime.combine(timezone.now().date(), datetime.time.max)

        orders_today = self.get_queryset().filter(date_ordered__range=(today_min, today_max))
        # orders_today = self.get_queryset().filter(date_ordered=datetime.datetime.now().day)
        serializer = self.get_serializer(orders_today, many=True)
        return Response(serializer.data)

    filter_backends = [DjangoFilterBackend]
    filter_class = OrderFilter


class ManufacturerViewSet(viewsets.ModelViewSet):
    serializer_class = ManufacturerSerializer
    queryset = Manufacturer.objects.all().order_by("-manu_num")
    permission_classes = (permissions.IsAdminUser,)

    # manufactures/address-busan/   부산에 위치한 제조업체 조회
    @action(methods=['get'], detail=False, url_path='address-busan', url_name='address_busan')
    def address_busan(self, request):
        manu_busan = self.get_queryset().filter(address__icontains='Busan')   # icontains로 대소문자 포함(busan, Busan)
        serializer = self.get_serializer(manu_busan, many=True)
        return Response(serializer.data)


class DeliveryViewSet(viewsets.ModelViewSet):
    serializer_class = DeliverySerializer
    queryset = Delivery.objects.all().order_by("-transport")
    permission_classes = (permissions.IsAdminUser,)

    # deliveries/completed/   완료된 배송 조회
    @action(methods=['get'], detail=False, url_path='completed', url_name='completed')
    def completed(self, request):
        deliveries_started = self.get_queryset().filter(state='completed')
        serializer = self.get_serializer(deliveries_started, many=True)
        return Response(serializer.data)


class ReviewViewSet(viewsets.ModelViewSet):
    serializer_class = ReviewSerializer
    queryset = Review.objects.all().order_by("-review_num")
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)

    # reviews/image/   사진 있는 리뷰만 조회
    @action(methods=['get'], detail=False, url_path='image', url_name='image')
    def image(self, request):
        # for 문보다는 filter(image=True) 사용하기
        """
        reviews = self.get_queryset()
        reviews_images = []
        for review in reviews:
            if review.image:
                reviews_images.append(review)
            serializer = self.get_serializer(reviews_images, many=True)
            return Response(serializer.data)
        return Response('No review having images')
        """
        reviews_images = self.get_queryset().filter(image=True)
        serializer = self.get_serializer(reviews_images, many=True)
        return Response(serializer.data)
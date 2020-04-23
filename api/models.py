# -*- coding: utf-8 -*-
from django.db import models
from django.contrib.auth.models import User
# from django.utils.translation import ugettext_lazy as _   # 다국어 사이트를 위한 맞춤번역 (Form 과 admin) 나중에 적용
from django.utils import timezone
# from datetime import datetime   # timezone 으로 통일
# from django.db.models.signals import post_save   # 오류 발생하여 사용하지 않음
# from django.dispatch import receiver   # 오류 발생하여 사용하지 않음


# 자유도가 높은 AbstractBaseUser 를 사용하려 했으나 이미 테이블 생성 후 AUTH_USER_MODEL 변경하니 dependency 오류가 발생함
# 따라서 OneToOneField 로 방법을 바꿔서 유저 모델을 생성하였음
class MyUser(models.Model):
    # id 자동생성
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    # User 모델에 password, email, username, date_joined 이 존재하므로 생략
    # password = models.CharField('비밀번호', max_length=20)
    # email = models.EmailField('이메일 주소', max_length=200, unique=True)
    # name = models.CharField('이름', max_length=30)
    phone = models.CharField('전화번호', max_length=20)
    GENDER = (
        # (DB 저장값, admin 페이지 및 Form 표시값)
        ('male', '남성'),
        ('female', '여성'),
        ('neither', '선택 안함'),   # 'do not specify'
    )
    gender = models.CharField('성별',  max_length=10, choices=GENDER, default='male')
    date_joined = models.DateTimeField('가입일', default=timezone.now)   # auto_now_add=True 도 무방
    address = models.CharField('주소', max_length=100)
    date_of_birth = models.DateField('생년월일', null=True, blank=True)

    # Product 와의 관계 N:M
    # Product 클래스 생성 전이므로 클래스 명 'Product'로 관계 설정
    # Product 에 대해서 구매한 모든 유저들을 조회할 때 사용될 수 있으니 related_name='purchased_users' 지정
    product = models.ManyToManyField(
        'Product',
        through='Order',
        through_fields=('myuser', 'product'),
        related_name='purchased_users',
        verbose_name='구매한 상품',
    )

    class Meta:
        verbose_name = '유저'   # 모델 자체 이름
        # verbose_name 이 정의되어 있는 상태에서 verbose_name_plural 이 정의되지 않았으면, 자동으로 뒤에 s 하나를 붙여준다.
        verbose_name_plural = '유저'   # 복수형
        ordering = ('-date_joined',)   # 최신 가입순 # date_joined 속성 삭제

    def __str__(self):
        return self.name


class Product(models.Model):
    pro_num = models.AutoField('상품번호 PK', primary_key=True)   # PK 별도로 지정
    pro_name = models.CharField('상품명', max_length=100)
    inventory = models.IntegerField('재고량')
    price = models.IntegerField('단가')

    # Manufacturer 클래스 생성 전이므로 클래스 명 'Manufacturer'로 관계 설정
    '''
    ForeignKey 1:N 관계에서 1에 대해 N을 어떻게 표현할지 직관적으로 나타낼 수 있도록 related_name 추가. 
    related_name 을 명시하지 않고 ORM 쿼리 사용 시 장고가 자동으로 _set 을 붙여서 Manufacturer.product_set.all()으로 사용
    related_name='products'로 설정 시 더 깔끔하고 직관적으로 Manufacturer.products.all() 같이 사용가능
    '''
    manufacturer = models.ForeignKey(
        'Manufacturer',
        on_delete=models.CASCADE,
        related_name='products',
        max_length=50,
        verbose_name='제조업체',
    )
    supply_date = models.DateField('공급일자')
    supply_vol = models.IntegerField('공급량')

    class Meta:
        verbose_name = '상품'
        verbose_name_plural = '상품'
        ordering = ('-supply_date',)   # 최신 공급순

    def __str__(self):
        return self.pro_name


# MyUser 와 Product 의 중개 모델(intermediate model)
class Order(models.Model):
    # PK 는 Meta 클래스를 참고
    myuser = models.ForeignKey(MyUser,
                                on_delete=models.CASCADE,
                                related_name='orders',
                                verbose_name='유저')
    product = models.ForeignKey(Product,
                                on_delete=models.CASCADE,
                                related_name='orders',
                                verbose_name='상품')
    quantity = models.IntegerField('주문수량')
    '''
    # Order 의 destination 은 원래 MyUser 의 address 정보를 참조하려 하였으나 참조 무결성 제약조건에 어긋남
    # 외래키는 다른 릴레이션의 기본키를 참조하는 속성
    destination = models.ForeignKey(
        MyUser, to_field='address',
        on_delete=models.CASCADE,
        verbose_name=_('user address')
    )
    '''
    destination = models.CharField('배송지', max_length=100)
    date_ordered = models.DateTimeField('주문일자', default=timezone.now)   # editable=False 인자 불가
    message = models.CharField('주문요청메시지', max_length=300, blank=True)

    class Meta:
        # myuser 와 product 이 세트로 PK 가 되므로 unique 하게 설정
        unique_together = (
            ('myuser', 'product')
        )
        verbose_name = '주문'
        verbose_name_plural = '주문'
        ordering = ('-date_ordered',)  # 최신 주문순


class Manufacturer(models.Model):
    manu_num = models.AutoField('제조업체번호 PK', primary_key=True)   # PK 별도로 지정
    manu_name = models.CharField('제조업체명', max_length=50)
    phone = models.CharField('전화번호', max_length=20)
    address = models.CharField('주소', max_length=100)
    supervisor = models.CharField('담당자', max_length=30)

    class Meta:
        verbose_name = '제조업체'
        verbose_name_plural = '제조업체'
        ordering = ('-manu_num',)   # 최신 등록순

    def __str__(self):
        return self.manu_name


class Delivery(models.Model):
    delivery_num = models.AutoField('배송번호 PK', primary_key=True)   # PK 별도로 지정
    '''
    Order 테이블을 참조하기 위해선 Order 의 PK 를 가져오면 된다.
    Order 의 PK 는 두 개의 복합키(myuser, product)로 이루어져 있는데, 가져오는 방식은 아래처럼 단순하다. 
    '''
    order = models.ForeignKey('Order',
                              on_delete=models.CASCADE,
                              related_name='deliveries',
                              verbose_name='주문식별')

    date_delivered = models.DateTimeField('배송일자', default=timezone.now)
    transport = models.CharField('운송장번호', max_length=20)
    STATE = (
        ('preparing', '상품준비중'),
        ('departure', '배송출발'),
        ('in_progress', '배송중'),
        ('completed', '배송완료'),
    )
    state = models.CharField('배송상태', max_length=20, choices=STATE, default='preparing')

    class Meta:
        verbose_name = '배송'
        verbose_name_plural = '배송'
        ordering = ('-transport',)   # 최신 운송장번호순

    def __str__(self):
        return self.delivery_num


class Review(models.Model):
    review_num = models.AutoField('글번호 PK', primary_key=True)   # PK 별도로 지정
    myuser = models.ForeignKey('MyUser',
                               on_delete=models.CASCADE,
                               related_name='reviews',
                               default=1,
                               verbose_name='유저')
    # Order 테이블의 복합기본키(myuser, product)를 가져온다.
    order = models.ForeignKey('Order',
                              on_delete=models.CASCADE,
                              related_name='reviews',
                              verbose_name='주문식별')
    title = models.CharField('글제목', max_length=100, default='')
    # ImageField 사용시 필수인 이미지처리 라이브러리 pillow 를 설치한다
    image = models.ImageField('글사진', blank=True)   # 썸네일 생성 생략
    content = models.TextField('글내용', default='')
    pub_date = models.DateTimeField('작성일자', default=timezone.now)

    class Meta:
        verbose_name = '리뷰'
        verbose_name_plural = '리뷰'
        ordering = ('-review_num',)   # 최신 리뷰순

    def __str__(self):
        return '[{}] {}'.format(self.myuser.name, self.title)

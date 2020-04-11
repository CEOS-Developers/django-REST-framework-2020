from django.db import models
from django.contrib.auth.models import User
from django.utils.translation import ugettext_lazy as _   # 다국어 사이트를 위한 맞춤번역 (Form 과 admin)
from django.utils import timezone
# from datetime import datetime
# from django.db.models.signals import post_save   # 오류 발생하여 사용하지 않음
# from django.dispatch import receiver   # 오류 발생하여 사용하지 않음


# 자유도가 높은 AbstractBaseUser 를 사용하려 했으나 이미 테이블 생성 후 AUTH_USER_MODEL 변경하니 dependency 오류가 발생함
# 따라서 OneToOneField 로 방법을 바꿔서 유저 모델을 생성하였음
class MyUser(models.Model):
    # id 자동생성
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    password = models.CharField(_('password'), max_length=20)
    email = models.EmailField(_('email address'), max_length=200, unique=True)
    name = models.CharField(_("user's name"), max_length=30)
    phone = models.CharField(_('phone number'), max_length=20)
    GENDER = (
        # (DB 저장값, admin 페이지 및 Form 표시값)
        ('male', _('male')),
        ('female', _('female')),
        ('neither', _('neither')),   # 'do not specify'
    )
    gender = models.CharField(_('gender'),  max_length=10, choices=GENDER, default='male')
    date_joined = models.DateTimeField(_('date joined'), default=timezone.now)   # auto_now_add=True 도 무방
    location = models.CharField(_('address'), max_length=100)
    date_of_birth = models.DateField(_('date of birth'), null=True, blank=True)

    # Product 와의 관계 N:M
    # Product 클래스 생성 전이므로 클래스 명 'Product'로 관계 설정
    pro_num = models.ManyToManyField(
        'Product',
        through='Order',
        through_fields= ('user_id', 'pro_num'),
        verbose_name=_('number of product'),
    )

    class Meta:
        verbose_name = _('User')   # 모델 자체 이름
        # verbose_name 이 정의되어 있는 상태에서 verbose_name_plural 이 정의되지 않았으면, 자동으로 뒤에 s 하나를 붙여준다.
        verbose_name_plural = _('Users')   # 복수형
        ordering = ('-date_joined',)   # 최신 가입순

    def __str__(self):
        return self.name


class Product(models.Model):
    pro_num = models.AutoField(_('number of product (PK)'), primary_key=True)   # PK 별도로 지정
    name = models.CharField(_('name of product'), max_length=100)
    inventory = models.IntegerField(_('inventory'))
    price = models.IntegerField(_('price of product'))

    # Manufacturer 클래스 생성 전이므로 클래스 명 'Manufacturer'로 관계 설정
    manu_num = models.ForeignKey(
        'Manufacturer',
        on_delete=models.CASCADE,
        max_length=50,
        verbose_name=_('number of manufacturer')
    )
    supply_date = models.DateTimeField(_('supply date'))
    supply_vol = models.IntegerField(_('supply volume'))

    def __str__(self):
        return self.pro_num


# MyUser 와 Product 의 중개 모델(intermediate model)
class Order(models.Model):
    # PK 는 Meta 클래스를 참고
    user_id = models.ForeignKey(
        MyUser,
        on_delete=models.CASCADE,
    )
    pro_num = models.ForeignKey(Product, on_delete=models.CASCADE)
    many = models.IntegerField(_('quantity ordered'))
    '''
    # Order 의 destination 은 원래 MyUser 의 location 정보를 참조하려 하였으나 참조 무결성 제약조건에 어긋남
    # 외래키는 다른 릴레이션의 기본키를 참조하는 속성
    destination = models.ForeignKey(
        MyUser, to_field='location',
        on_delete=models.CASCADE,
        verbose_name=_('user address')
    )
    '''
    destination = models.CharField(_('destination'), max_length=100)
    date_ordered = models.DateTimeField(_('date ordered'), default=timezone.now)   # editable=False 인자 불가
    message = models.CharField(_('request message'), max_length=300, blank=True)

    class Meta:
        # user_id 와 pro_num 이 세트로 PK 가 되므로 unique 하게 설정
        unique_together = (
            ('user_id', 'pro_num')
        )


class Manufacturer(models.Model):
    manu_num = models.AutoField(_('number of manufacturer (PK)'), primary_key=True)   # PK 별도로 지정
    manu_name = models.CharField(_('name of manufacturer'), max_length=50)
    phone = models.CharField(_('phone number'), max_length=20)
    location = models.CharField(_('address'), max_length=100)
    supervisor = models.CharField(_("supervisor's name"), max_length=30)

    class Meta:
        verbose_name = _('Manufacturer')
        verbose_name_plural = _('Manufacturers')
        ordering = ('-manu_num',)   # 최신 등록순
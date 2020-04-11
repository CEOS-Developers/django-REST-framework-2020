from django.db import models
from django.contrib.auth.models import (
    BaseUserManager, AbstractBaseUser, PermissionsMixin
)
from django.utils import timezone
from django.utils.translation import ugettext_lazy as _   # 다국어 사이트를 위한 맞춤번역 (Form과 admin)


'''
모델을 관리하는 클래스인 매니저를 만들어 준다. 모든 장고 모델은 Manager 를 통하여 QuerySet 을 받는다. 
즉, 데이터베이스에서 쿼리할 때는 무조건 manager 를 통한다.
BaseUserManager 클래스를 상속받는 커스텀 매니저에는 create_user, create_superuser 두 개의 메소드를 구현해야 한다.
'''
class MyUserManager(BaseUserManager):
    # 일반 유저 생성 - 주어진 개인정보로 User 인스턴스 생성(Create and save)
    def create_user(self, email, name, phone, gender, date_joined, location, date_of_birth, password=None):
        # 디폴트 값이 없는 파라미터부터 선언되어야 하므로 password가 제일 뒤에 놓인다. (elif: SyntaxError)
        if not email:
            raise ValueError(_('Users must have an email address'))

        user = self.model(
            email=self.normalize_email(email),
            name=name,
            phone=phone,
            gender=gender,
            date_joined=date_joined,
            location=location,
            date_of_birth=date_of_birth,
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    # 관리자 유저 생성
    def create_superuser(self, email, name, password, phone, gender, date_joined, location, date_of_birth):
        user = self.create_user(
            email,
            name=name,
            password=password,
            phone=phone,
            gender=gender,
            date_joined=date_joined,
            location=location,
            date_of_birth=date_of_birth,
        )
        user.is_admin = True
        user.save(using=self._db)
        return user


class MyUser(AbstractBaseUser):
    # id는 자동생성
    email = models.EmailField(_('email address'), max_length=200, unique=True)
    name = models.CharField(_('name'), max_length=30, blank=True)
    phone = models.CharField(_('phone number'), max_length=20)
    GENDER = (
        # (DB 저장값, admin 페이지 및 Form 표시값)
        ('male', _('male')),
        ('female', _('female')),
        ('neither', _('neither')),   # 'do not specify'
    )
    gender = models.CharField(_('gender'),  max_length=10, choices=GENDER, default='male')
    date_joined = models.DateTimeField(_('date_joined'), default=timezone.now)   # auto_now_add=True도 무방
    location = models.CharField(max_length=100, blank=True)
    date_of_birth = models.DateField(null=True, blank=True)

    is_active = models.BooleanField(_('is_active'), default=True)   #활성화 여부
    is_staff = models.BooleanField(_('is_staff'),default=False)   #관리자 여부

    # Manager는 무조건 모든 모델에 objects 라는 이름으로 존재한다.
    objects = MyUserManager()

    # 커스텀 유저 모델의 unique identifier (unique=True 옵션이 설정되어 있어야 한다)
    USERNAME_FIELD = 'email'

    '''
    기본 authentication model 을 MyUser 모델로 대체하고 있다. 
    따라서 관리자 계정을 만들 때(python manage.py superuser) 필요한 필드들을 새로 명시해 주어야 한다.
    USERNAME_FIELD에 명시된 필드와, 패스워드는 기본적으로 요구하기 때문에, 따로 명시하지 않아도 된다.
    '''
    REQUIRED_FIELDS = ['name', 'phone', 'gender', 'date_joined', 'location', 'date_of_birth']

    class Meta:
        db_table = 'myusers'   # 해당 모델과 매핑되는 데이터베이스 테이블의 이름
        verbose_name = _('user')   # 모델 자체 이름
        # verbose_name 이 정의되어 있는 상태에서 verbose_name_plural 이 정의되지 않았으면, 자동으로 뒤에 s 하나를 붙여준다.
        verbose_name_plural = _('users')   # 복수형
        ordering = ('-date_joined',)   # 최신 가입순

    def __str__(self):
        return self.name





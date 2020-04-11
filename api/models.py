from django.db import models
from django.contrib.auth.models import User
from django.utils.translation import ugettext_lazy as _   # 다국어 사이트를 위한 맞춤번역 (Form 과 admin)
from django.utils import timezone
# from django.db.models.signals import post_save   # 오류 발생하여 사용하지 않음
# from django.dispatch import receiver   # 오류 발생하여 사용하지 않음


class MyUser(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    password = models.CharField(_('password'), max_length=20)
    email = models.EmailField(_('email address'), max_length=200, unique=True)
    name = models.CharField(_('name'), max_length=30)
    phone = models.CharField(_('phone number'), max_length=20)
    GENDER = (
        # (DB 저장값, admin 페이지 및 Form 표시값)
        ('male', _('male')),
        ('female', _('female')),
        ('neither', _('neither')),   # 'do not specify'
    )
    gender = models.CharField(_('gender'),  max_length=10, choices=GENDER, default='male')
    date_joined = models.DateTimeField(_('date joined'), default=timezone.now)   # auto_now_add=True 도 무방
    location = models.CharField(_('location'), max_length=100, blank=True)
    date_of_birth = models.DateField(_('date of birth'), null=True, blank=True)

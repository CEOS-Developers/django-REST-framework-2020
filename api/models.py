from django.core.validators import RegexValidator
from django.db import models
from django.contrib.auth.models import User


# [제약조건]
# 1. 1:1과 1:n의 관계 포함
# 2. 각 모델에 필드 최소 3개 이상 포함
# 3. 서비스 관련 모델 3개 이상 + 유저 모델 1개 구현 (단, 유저는 필수 아님)


# 하나의 영화관(db : megabox)에서 상영되는 영화, 누적관객 수, 상영날짜 등으로 모델링

class Director(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Country(models.Model):
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name


class Genre(models.Model):
    # choices
    GENRE_CHOICES = {
        ('SF', 'science_fiction'),
        ('DR', 'drama'),
        ('RM', 'romance'),
        ('AC', 'action'),
        ('HR', 'horror'),
        ('DS', 'disaster'),
        ('DC', 'documentary'),
        ('MS', 'mystery'),
        ('FT', 'fantasy'),
        ('CM', 'comedy'),
        ('SP', 'sport'),
        ('WR', 'war'),
        ('EP', 'epic'),
        ('MU', 'musical'),
        ('AD', 'adventure'),
        ('WS', 'western'),
        ('TH', 'thriller')
    }
    name = models.CharField(max_length=20, choices=GENRE_CHOICES, unique=True)

    # Movie.objects.filter(genre='SF').count() 장르별 통계
    # name = models.CharField(max_length=20)
    def __str__(self):
        return self.name


class Movie(models.Model):
    title = models.CharField(max_length=200)
    director = models.ForeignKey('Director', on_delete=models.CASCADE, related_name='movies')
    release_date = models.DateField()
    running_time = models.IntegerField()  # minutes 단위
    country = models.ForeignKey('Country', on_delete=models.SET_DEFAULT, default="Korea", related_name='movies')
    genre = models.ForeignKey('Genre', on_delete=models.SET_DEFAULT, default="SF", related_name='movies')

    def __str__(self):
        return self.title


# user model
class Member(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    nickname = models.CharField(max_length=100, unique=True)
    phone_number = models.CharField(max_length=100, validators=[RegexValidator(r'^[0-9]+$',
                                                                               'Enter a valid phone number.')])  # 제약조건 010-xxxx-xxxx
    RANK_CHOICES = {
        ('V', 'vip'),
        ('G', 'gold'),
        ('S', 'silver')
    }
    rank = models.CharField(max_length=10, choices=RANK_CHOICES)

    def __str__(self):
        return self.nickname


class Watcher(models.Model):  # user- 1toN -watcher- Nto1 - movie
    member = models.ForeignKey('Member', on_delete=models.CASCADE, related_name='watchers')
    movie = models.ForeignKey('Movie', on_delete=models.CASCADE, related_name='watchers')
    watched_at = models.DateField()


class Workers(models.Model):  # 영화관 직원 관리
    name = models.CharField(max_length=100)
    birth = models.DateField()
    join_date = models.DateField()  # 입사날짜

    GENDER_CHOICES = {
        ('F', 'female'),
        ('M', 'male')
    }
    POSITION_CHOICES = {
        ('CO', 'counter'),
        ('CL', 'cleaning'),
        ('FD', 'food'),
        ('TK', 'ticket')
    }
    gender = models.CharField(max_length=10, choices=GENDER_CHOICES)
    position = models.CharField(max_length=10, choices=POSITION_CHOICES, null=True, blank=True)

    def __str__(self):
        return self.name

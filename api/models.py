from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    GENDER_CHOICES = (
        (0, 'Male'),
        (1, 'Female'),
        (2, 'Not to disclose')
    )

    email = models.EmailField(verbose_name='email', max_length=255, unique=True)
    username = models.CharField(max_length=30)
    gender = models.SmallIntegerField(choices=GENDER_CHOICES)
    phone = models.CharField(max_length=11)

    USERNAME_FIELD = 'email'    # 로그인을 이메일로 하기 위해
    REQUIRED_FIELDS = []        # 필수로 받고 싶은 필드들 넣기. 원래 소스 코드엔 email 필드가 들어가지만, 비워줘야 함.

    def __str__(self):
        return "%d. %s" % (self.pk, self.username)


class Movie(models.Model):
    title = models.CharField(max_length=64)
    director = models.CharField(max_length=64)
    genre = models.CharField(max_length=32)
    country = models.CharField(max_length=32)
    rel_day = models.DateTimeField(verbose_name='release_day')
    poster = models.ImageField(blank=True, null=True, upload_to='')

    def __str__(self):
        return self.title


class TimeTable(models.Model):
    movie = models.ForeignKey('Movie', on_delete=models.CASCADE, related_name='timetable')
    time = models.DateTimeField()

    def __str__(self):
        return "%s - %s" % (self.movie.title, self.time)


class Review(models.Model):
    RATE_CHOICES = (            # 별모양 5개에서 채우는 걸로 하고 싶은데, 나중에 view 에서 구현 해야할듯
        (1, 'worst'),
        (2, 'bad'),
        (3, 'just'),
        (4, 'good'),
        (5, 'best'),
    )
    user = models.ForeignKey('User', on_delete=models.CASCADE, related_name='reviews')
    movie = models.ForeignKey('Movie', on_delete=models.CASCADE, related_name='reviews')
    rate = models.SmallIntegerField(choices=RATE_CHOICES)
    comment = models.CharField(max_length=255)

    def __str__(self):
        return "%s - %s : %s점" % (self.movie.title, self.user.username, self.rate)


class Booking(models.Model):
    user = models.ForeignKey('User', on_Delete=models.CASCADE, related_name='ticket')
    movie = models.ForeignKey('Movie', in_delete=models.CASCADE, related_name='reserved')
    movie_time = models.ForeignKey('TimeTable', on_delete=models.CASCADE, related_name='ticket')
    booking_time = models.DateTimeField(auto_now_add=True)
    num = models.IntegerField()

    def __str__(self):
        return "Name: %s, %s %d명" % (self.user.username, self.movie.title, self.num)

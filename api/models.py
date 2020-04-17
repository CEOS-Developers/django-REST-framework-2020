from django.db import models
from django.contrib.auth.models import AbstractUser
from phonenumber_field.modelfields import PhoneNumberField  # PhoneNumber library 설치.


class User(AbstractUser):
    GENDER_CHOICES = (
        (0, 'Male'),
        (1, 'Female'),
        (2, 'Not to disclose')
    )

    email = models.EmailField(verbose_name='email', max_length=255, unique=True)
    username = models.CharField(max_length=30)
    gender = models.SmallIntegerField(choices=GENDER_CHOICES)
    phone = PhoneNumberField(null=False, blank=False, unique=True)
    wish_list = models.ManyToManyField('Movie', related_name='wished_bys')  # 하나의 유저가 여러 영화에 대해, 하나의 영화를 여러 유저가 사용

    USERNAME_FIELD = 'email'  # 로그인을 이메일로 하기 위해
    REQUIRED_FIELDS = ['username', 'gender', 'phone']  # 필수로 받고 싶은 필드들 넣기. 원래 소스 코드엔 email 필드가 들어가지만, 비워줘야 함.
    # REQUIRED_FIELD 에 'username'을 추가하지 않으면 error 발생 : USERNAME_FIELD = 'email'로 설정했더라도 AbstractUser 모델에서 해당 인수를 기대

    def __str__(self):
        return "%d. %s" % (self.pk, self.username)


class Movie(models.Model):
    title = models.CharField(max_length=64)
    country = models.ForeignKey('Country', on_delete=models.CASCADE, related_name='movies')
    rel_day = models.DateField(verbose_name='release_day')
    is_on_now = models.BooleanField(default=False)
    poster = models.ImageField(blank=True, null=True, upload_to='')

    def __str__(self):
        return self.title


class Country(models.Model):        # Movie 제작 국가는 하나, 한 국가에는 여러 영화가 있음
    name = models.CharField(max_length=32)


class Genre(models.Model):
    GENRE_CHOICES = (
        ('DR', 'Drama'),
        ('CM', 'Comedy'),
        ('Th', 'Thriller'),
        ('RM', 'Romance'),
        ('AC', 'Action'),
        ('HR', 'Horror'),
        ('CR', 'Crime'),
        ('AV', 'Adventure'),
        ('MS', 'Mystery'),
        ('FM', 'Family'),
        ('FT', 'Fantasy'),
        ('SF', 'Sci-Fi'),
        ('MU', 'Music'),
        ('AM', 'Animation'),
        ('BO', 'Biography'),
        ('HS', 'History'),
        ('MS', 'Musical'),
        ('WR', 'War'),
        ('SP', 'Sport'),
        ('ID', 'indeterminate')
    )

    movie = models.ForeignKey('Movie', on_delete=models.CASCADE, related_name='genres')  # 영화는 여러 장르가 복합될 수 있음
    name = models.CharField(choices=GENRE_CHOICES, max_length=15)


class Director(models.Model):
    # 영화에 감독이 여러명일 수도 있고, 감독이 여러 영화를 만들 수 도 있음
    movie = models.ManyToManyField('Movie', related_name='directors')
    name = models.CharField(max_length=30)


class TimeTable(models.Model):
    movie = models.ForeignKey('Movie', on_delete=models.CASCADE, related_name='timetables')
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()

    def __str__(self):
        return "%s : %s ~ %s" % (self.movie.title, self.start_time, self.end_time)


class Review(models.Model):
    RATE_CHOICES = (
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
    user = models.ForeignKey('User', on_delete=models.CASCADE, related_name='bookings')
    movie = models.ForeignKey('Movie', on_delete=models.CASCADE, related_name='bookings')
    movie_time = models.ForeignKey('TimeTable', on_delete=models.CASCADE, related_name='bookings')
    booking_time = models.DateTimeField(auto_now_add=True)
    num_people = models.IntegerField()

    def __str__(self):
        return "Name: %s, %s %d명" % (self.user.username, self.movie.title, self.num_people)

from django.db import models


class Movie(models.Model):
    title = models.CharField(max_length=64)
    director = models.CharField(max_length=64)
    genre = models.CharField(max_length=32)
    country = models.CharField(max_length=32)
    rel_day = models.DateTimeField(blank=True, null=True, verbose_name='개봉날짜')
    poster = models.ImageField()

    def __str__(self):
        return self.title


class Review(models.Model):
    # User model 구현후 추가 예정
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    rate = models.IntegerField()    # User model 사용 예정 -> 평점 함수 구현
    comment = models.CharField(max_length=255)    # User model 사용 예정

    def __str__(self):
        return str(self.movie) + ' ' + str(self.rate)   # 임시 형태

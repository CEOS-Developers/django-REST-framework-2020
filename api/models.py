from django.db import models


# [제약조건]
# 1. 1:1과 1:n의 관계 포함
# 2. 각 모델에 필드 최소 3개 이상 포함
# 3. 서비스 관련 모델 3개 이상 + 유저 모델 1개 구현 (단, 유저는 필수 아님)


# 하나의 영화관(db : megabox)에서 상영되는 영화, 누적관객 수, 상영날짜 등으로 모델링

class Movie(models.Model):
    title = models.CharField(max_length=200, primary_key=True)
    director = models.CharField(max_length=100)
    release_year = models.IntegerField()
    running_time = models.IntegerField()  # minutes 단위
    country = models.CharField(max_length=100)
    genre = models.CharField(max_length=100)

    def givetitle(self):
        return self.title

    def __str__(self):
        return self.title


class ScreeningDates(models.Model):  # 시기별 누적 관객수
    title = models.ForeignKey('Movie', on_delete=models.CASCADE)
    start_date = models.DateTimeField()
    finished_date = models.DateTimeField(null=True)
    total_audience = models.IntegerField()

    def __str__(self):
        return str(self.title)


class GenreStat(models.Model):  # 영화 장르별 통계
    genre = models.ForeignKey('Movie', on_delete=models.CASCADE)
    genre_count = models.IntegerField()

    def __str__(self):
        return str(self.genre)


class CountryStat(models.Model):  # 영화 국가별 통계
    country = models.ForeignKey('Movie', on_delete=models.CASCADE)
    country_count = models.IntegerField()

    def __str__(self):
        return str(self.country)


class Workers(models.Model):  # 영화관 직원 관리
    name = models.CharField(max_length=100)
    birth = models.DateTimeField()
    age = models.IntegerField()
    gender = models.CharField(max_length=100)
    position = models.CharField(max_length=200, null=True)  # counter, cleaning, food, ticketcheck

    def __str__(self):
        return self.name

from django.db import models


# 모델링 과제를 이곳에서 해주시면 됩니다! (주석은 나중에 지우셔도 돼요!)

class Member(models.Model):
    email = models.CharField(max_length=20)
    password = models.CharField(max_length=20)
    name = models.CharField(max_length=20)
    tel = models.CharField(max_length=20)

    def __str__(self):
        return self.id


class Branch(models.Model):
    location = models.CharField(max_length=50)
    total_theater = models.IntegerField()

    def __str__(self):
        return self.id


class Theater(models.Model):
    total_seat = models.IntegerField()

    def __str__(self):
        return self.id


class Seat(models.Model):
    theater = models.ForeignKey('Theater', on_delete=models.CASCADE)
    is_reservation = models.BooleanField(default=False)

    def __str__(self):
        return self.id


class Schedule(models.Model):
    theater = models.ForeignKey('Theater', on_delete=models.CASCADE)
    branch = models.ForeignKey('Branch', on_delete=models.CASCADE)
    schedule_date = models.DateField()
    schedule_time = models.TimeField()

    def __str__(self):
        return self.id


class Movie(models.Model):
    schedule = models.ForeignKey('Schedule', on_delete=models.CASCADE)
    movie_title = models.CharField(max_length=50)
    genre = models.CharField(max_length=20)

    def __str__(self):
        self.id


class ReservationTicket(models.Model):
    schedule = models.ForeignKey('Schedule', on_delete=models.CASCADE)
    movie = models.ForeignKey('Movie', on_delete=models.CASCADE)
    theater = models.ForeignKey('Theater', on_delete=models.CASCADE)
    seat = models.ForeignKey('Seat', on_delete=models.CASCADE)
    branch = models.ForeignKey('Branch', on_delete=models.CASCADE)

    def __str__(self):
        self.id


class Pay(models.Model):
    reservation = models.ForeignKey('ReservationTicket', on_delete=models.CASCADE,related_name='reservation_id')
    member = models.OneToOneField(
        'Member',
        on_delete=models.CASCADE
    )
    payment_date = models.DateField()
    price = models.IntegerField()
    payment_option = models.CharField(max_length=20)
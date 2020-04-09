from django.db import models


class Member(models.Model):
    email = models.CharField(max_length=20)
    password = models.CharField(max_length=20)
    name = models.CharField(max_length=20)
    tel = models.CharField(max_length=20)

    def __str__(self):
        return self.id


class Branch(models.Model):
    branch_name = models.CharField(max_length=20, primary_key=True)
    location = models.CharField(max_length=50)
    total_theater = models.IntegerField()

    def __str__(self):
        return self.branch_name


class Theater(models.Model):
    theater_no = models.CharField(max_length=10, primary_key=True)
    total_seat = models.IntegerField()
    branch = models.ForeignKey('Branch', on_delete=models.CASCADE)

    def __str__(self):
        return self.theater_no


class Seat(models.Model):
    seat_no = models.IntegerField(primary_key=True)
    is_reservation = models.BooleanField(default=False)
    branch = models.ForeignKey('Branch', on_delete=models.CASCADE)
    theater = models.ForeignKey('Theater', on_delete=models.CASCADE)

    def __str__(self):
        return self.seat_no


class Movie(models.Model):
    movie_title = models.CharField(max_length=50)
    genre = models.CharField(max_length=20)

    def __str__(self):
        self.id


class Schedule(models.Model):
    schedule_date = models.DateField()
    schedule_time = models.TimeField()
    movie = models.ForeignKey('Movie', on_delete=models.CASCADE)
    branch = models.ForeignKey('Branch', on_delete=models.CASCADE)
    theater = models.ForeignKey('Theater', on_delete=models.CASCADE)

    def __str__(self):
        return self.id


class ReservationTicket(models.Model):
    schedule = models.ForeignKey('Schedule', on_delete=models.CASCADE)
    movie = models.ForeignKey('Movie', on_delete=models.CASCADE)
    theater = models.ForeignKey('Theater', on_delete=models.CASCADE)
    seat = models.ForeignKey('Seat', on_delete=models.CASCADE)
    branch = models.ForeignKey('Branch', on_delete=models.CASCADE)

    def __str__(self):
        self.id


class Pay(models.Model):
    member = models.OneToOneField(
        'Member',
        on_delete=models.CASCADE
    )
    payment_date = models.DateField()
    price = models.IntegerField()
    payment_option = models.CharField(max_length=20)
    reservation = models.ForeignKey('ReservationTicket', on_delete=models.CASCADE)

    def __str__(self):
        self.id

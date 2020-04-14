from django.db import models
from django.contrib.auth.base_user import BaseUserManager, AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin


class UserManager(BaseUserManager):
    use_in_migrations = True

    def create_user(self, email, tel, password=None):
        if not email:
            raise ValueError('must have user email')
        user = self.model(
            email=self.normalize_email(email),
            tel=tel
        )
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, tel, password):
        user = self.create_user(
            email=self.normalize_email(email),
            password=password,
            tel=tel
        )
        user.is_admin = True
        user.is_superuser = True
        user.is_staff = True
        user.save(using=self._db)
        return user


class User(AbstractBaseUser, PermissionsMixin):
    objects = UserManager()

    email = models.EmailField(
        max_length=255,
        unique=True,
    )
    tel = models.CharField(
        max_length=20,
        null=False,
        unique=True
    )
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    date_joined = models.DateTimeField(auto_now_add=True)
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['tel']

    def __str__(self):
        return self.id


class Branch(models.Model):
    name = models.CharField(max_length=20, unique=True)
    location = models.CharField(max_length=50)

    def __str__(self):
        return self.id


class Screen(models.Model):
    name = models.CharField(max_length=10, primary_key=True)
    branch = models.ForeignKey('Branch', on_delete=models.CASCADE, related_name='theaters')

    def __str__(self):
        return self.id


class Movie(models.Model):
    title = models.CharField(max_length=50)
    genre = models.CharField(max_length=20)

    def __str__(self):
        return self.id


class Schedule(models.Model):
    time = models.DateTimeField()
    movie = models.ForeignKey('Movie', on_delete=models.CASCADE, related_name='movie')
    branch = models.ForeignKey('Branch', on_delete=models.CASCADE, related_name='branch')
    screen = models.ForeignKey('Screen', on_delete=models.CASCADE, related_name='screen')

    def __str__(self):
        return self.id


class Seat(models.Model):
    seat_no = models.IntegerField(primary_key=True)
    branch = models.ForeignKey('Branch', on_delete=models.CASCADE)
    screen = models.ForeignKey('Screen', on_delete=models.CASCADE)

    def __str__(self):
        return self.seat_no

    def is_reserved(self, time):
        schedule = Schedule.objects.filter(time=time, movie=self.movie, branch=self.branch, screen=self.screen)
        return schedule.reservation_ticket_set.filter(seat=self).exists()


class ReservationTicket(models.Model):
    user = models.ForeignKey('User', on_delete=models.CASCADE, related_name='user')
    schedule = models.ForeignKey('Schedule', on_delete=models.CASCADE, related_name='schedule')
    seat = models.ForeignKey('Seat', on_delete=models.CASCADE, related_name='seat')

    def __str__(self):
        return self.id


class Pay(models.Model):
    payment_date = models.DateField()
    price = models.IntegerField()
    payment_option = models.CharField(max_length=20)
    member = models.ForeignKey('User', on_delete=models.CASCADE)
    reservation = models.ForeignKey('ReservationTicket', on_delete=models.CASCADE)

    def __str__(self):
        return self.id

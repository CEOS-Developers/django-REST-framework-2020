from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    def __int__(self):
        return self.id
    # user_id = models.IntegerField(null=False, default=0, unique=True)
    # name = models.CharField(null=False, default='', max_length=100)
    # password = models.CharField(max_length=200)
    # email = models.EmailField(max_length=255, unique=True)


class Major(models.Model):
    def __str__(self):
        return self.name

    num = models.IntegerField(default=0, primary_key=True)
    name = models.CharField(max_length=200)


class Student(models.Model):
    def __int__(self):
        return self.std_id

    # std_id = models.ForeignKey(User, on_delete=models.CASCADE, unique=True, primary_key=True, related_name="std_id")
    std_id = models.OneToOneField(User, on_delete=models.CASCADE, related_name="std_id")
    major = models.ForeignKey(Major, on_delete=models.CASCADE, related_name="major")
    grade = models.IntegerField(default=1)
    credits_available = models.IntegerField(default=18)
    current_credits = models.IntegerField(default=0)


class Professor(models.Model):
    def __str__(self):
        return self.prof_name

    # prof_id = models.IntegerField(default=0)
    name = models.CharField(max_length=200)
    major = models.ForeignKey(Major, on_delete=models.CASCADE)


class Course(models.Model):
    def __int__(self):
        return self.code

    code = models.IntegerField(default=0, unique=True)
    name = models.CharField(max_length=200)
    credit = models.IntegerField(default=0)
    professor = models.ForeignKey(Professor, null=True, on_delete=models.CASCADE, related_name="prof")
    classroom = models.CharField(max_length=200)
    WEEKDAY_CHOICE = [
        ('Mon', 'Monday'),
        ('Tue', 'Tuesday'),
        ('Wed', 'Wednesday'),
        ('Thu', 'Thursday'),
        ('Fri', 'Friday')
    ]
    weekday = models.CharField(max_length=20, choices=WEEKDAY_CHOICE)  # 강의 요일
    start_time = models.TimeField(auto_now=False, auto_now_add=False, null=True)  # 강의시간
    finish_time = models.TimeField(auto_now=False, auto_now_add=False, null=True)


class Basket(models.Model):
    def __int__(self):
        return self.course

    course = models.ForeignKey(Course, null=True, on_delete=models.CASCADE)
    student = models.ForeignKey(Student, null=True, on_delete=models.CASCADE)


class Registration(models.Model):
    def __int__(self):
        return self.course

    course = models.ForeignKey(Course, null=True, on_delete=models.CASCADE, related_name="registrations")
    student = models.ForeignKey(Student, null=True, on_delete=models.CASCADE)
    succeed_at = models.DateTimeField(auto_now=True)

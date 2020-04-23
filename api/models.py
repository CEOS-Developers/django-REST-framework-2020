from django.db import models
from django.contrib.auth.models import User
import datetime


class Major(models.Model):
    def __str__(self):
        return self.name

    num = models.IntegerField(default=0, primary_key=True)
    name = models.CharField(max_length=200)


class Student(models.Model):
    def __int__(self):
        return self.std_id

    std_id = models.BigIntegerField(default=0, primary_key=True)
    major = models.ForeignKey(Major, on_delete=models.CASCADE, related_name="major")
    grade = models.IntegerField(default=1)
    credits_available = models.IntegerField(default=18)


class Professor(models.Model):
    def __str__(self):
        return self.prof_name

    prof_id = models.IntegerField(default=0)
    prof_name = models.CharField(max_length=200)
    prof_major = models.ForeignKey(Major, on_delete=models.CASCADE)


class Course(models.Model):
    def __int__(self):
        return self.code

    code = models.IntegerField(default=0)
    name = models.CharField(max_length=200)
    credit = models.IntegerField(default=0)
    professor = models.ForeignKey(Professor, null=True, on_delete=models.CASCADE, related_name="courses")
    classroom = models.CharField(max_length=200)
    weekday = models.CharField(max_length=100, default='')  # 강의 요일
    start_time = models.TimeField(auto_now=False, auto_now_add=False, null=True)  # 강의시간
    finish_time = models.TimeField(auto_now=False, auto_now_add=False, null=True)


class Basket(models.Model):
    def __str__(self):
        return self.course

    course = models.ForeignKey(Course, null=True, on_delete=models.CASCADE)
    student = models.ForeignKey(Student, null=True, on_delete=models.CASCADE)


class Registration(models.Model):
    def __str__(self):
        return self.course

    course = models.ForeignKey(Course, null=True, on_delete=models.CASCADE, related_name="registrations")
    student = models.ForeignKey(Student, null=True, on_delete=models.CASCADE)
    current_credits = models.IntegerField(default=0)
    succeed_at = models.DateTimeField(auto_now=True)

from django.db import models
from django.contrib.auth.models import User
import datetime


class Major(models.Model):
    def __str__(self):
        return self.major_name

    num = models.IntegerField(default=0, primary_key=True)
    name = models.CharField(max_length=200)


class Student(models.Model):
    std_id = models.BigIntegerField(primary_key=True)
    std_major = models.ForeignKey(Major, on_delete=models.CASCADE, related_name="major")
    grade = models.IntegerField(default=1)
    credits_available = models.IntegerField(default=18)


class Professor(models.Model):
    def __str__(self):
        return self.prof_name

    prof_id = models.IntegerField(default=0, primary_key=True)
    prof_name = models.CharField(max_length=200)
    prof_major = models.ForeignKey(Major, on_delete=models.CASCADE)


class Course(models.Model):
    num = models.IntegerField(default=0, primary_key=True)
    name = models.CharField(max_length=200)
    credit = models.IntegerField(default=0)
    prof_name = models.ForeignKey(Professor, on_delete=models.CASCADE)
    classroom = models.CharField(max_length=200)
    weekday = models.CharField(max_length=100)  # 강의 요일
    start_time = models.TimeField(auto_now=False, auto_now_add=False)  # 강의시간
    finish_time = models.TimeField(auto_now=False, auto_now_add=False)


class Basket(models.Model):
    course_num = models.ForeignKey(Course, on_delete=models.CASCADE)
    std_id = models.ForeignKey(Student, on_delete=models.CASCADE)


class Registration(models.Model):
    course_num = models.ForeignKey(Course, on_delete=models.CASCADE, related_name="reg_crs")
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    current_credits = models.IntegerField(default=0)
    succeed_at = models.DateTimeField(auto_now=True)

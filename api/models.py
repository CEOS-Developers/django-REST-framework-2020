from django.db import models

# 모델링 과제를 이곳에서 해주시면 됩니다! (주석은 나중에 지우셔도 돼요!)

# [제약조건]
# 1. 1:1과 1:n의 관계 포함
# 2. 각 모델에 필드 최소 3개 이상 포함
# 3. 서비스 관련 모델 3개 이상 + 유저 모델 1개 구현 (단, 유저는 필수 아님)

import datetime
from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
# Create your models here.


class Student(models.Model):
    name = models.OneToOneField(User, on_delete=models.CASCADE)
    student_id = models.TextField(max_length=10)
    major = models.CharField(max_length=200)


class Course(models.Model):

    course_name = models.CharField(max_length=200)
    professor = models.CharField(max_length=200)
    course_num = models.CharField(max_length=200)
    capacity = models.IntegerField(default=0)
    total = models.IntegerField(default=0)
    credit = models.IntegerField(default=0)
    first = models.CharField(max_length=200)
    second = models.CharField(max_length=200)

    def __str__(self):
        return self.course_num


class Basket(models.Model):

    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    student_id = models.CharField(max_length=200)

    def __str__(self):
        return self.student_id

class Timetable(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    student_id = models.CharField(max_length=200)
    now = models.IntegerField(default=0)
    total = models.IntegerField(default=0)
    def __str__(self):
        return self.student_id
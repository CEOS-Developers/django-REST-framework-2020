from django.db import models

# 모델링 과제를 이곳에서 해주시면 됩니다! (주석은 나중에 지우셔도 돼요!)

# [제약조건]
# 1. 1:1과 1:n의 관계 포함
# 2. 각 모델에 필드 최소 3개 이상 포함
# 3. 서비스 관련 모델 3개 이상 + 유저 모델 1개 구현 (단, 유저는 필수 아님)

import datetime
from django.db import models
from django.utils import timezone
# Create your models here.


class Course(models.Model):

    course_name = models.CharField(max_length=200)
    professor = models.CharField(max_length=200)
    course_num = models.CharField(max_length=200)
    capacity = models.IntegerField(default=0)

    def __str__(self):
        return self.course_name


class Student(models.Model):

    student_name = models.CharField(max_length=200)
    student_id = models.CharField(max_length=200)
    major = models.CharField(max_length=200)
    password = models.CharField(max_length=200)

    def __str__(self):
        return self.student_name


class Basket(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    student_id = models.CharField(max_length=200)
    course_name = models.CharField(max_length=200)
    applied = models.BooleanField(default=False)

    def __str__(self):
        return self.student_id
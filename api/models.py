from django.db import models
from django.contrib.auth.models import User


class Major(models.Model):
    def __str__(self):
        return self.major_name
    major_num = models.IntegerField(default=0, primary_key=True)
    major_name = models.CharField(max_length=200)


class Student(models.Model):
    std_id = models.IntegerField(default=0, primary_key=True)
    std_major = models.OneToOneField(Major, on_delete=models.CASCADE)
    grade = models.IntegerField(default=1)
    credits_available = models.IntegerField(default=18)


class Professor(models.Model):
    def __str__(self):
        return self.prof_name
    prof_id = models.IntegerField(default=0, primary_key=True)
    prof_name = models.CharField(max_length=200)
    prof_major = models.ForeignKey(Major, on_delete=models.CASCADE)


class Course(models.Model):
    course_num = models.IntegerField(default=0, primary_key=True)
    course_name = models.CharField(max_length=200)
    credit = models.IntegerField(default=0)
    prof_name = models.ForeignKey(Professor, on_delete=models.CASCADE)
    classroom = models.CharField(max_length=200)
    timetable = models.CharField(max_length=200)  # 강의 시간


class Basket(models.Model):
    course_num = models.ForeignKey(Course, on_delete=models.CASCADE)
    std_id = models.ForeignKey(Student, on_delete=models.CASCADE)


class Registration(models.Model):
    course_num = models.ForeignKey(Course, on_delete=models.CASCADE, related_name="reg_crs")
    course_credit = models.ForeignKey(Course, on_delete=models.CASCADE, db_column="credit", related_name="reg_crd")
    std_id = models.ForeignKey(Student, on_delete=models.CASCADE)
    current_credits = models.IntegerField(default=0)
    max_credits = models.ForeignKey(Student, on_delete=models.CASCADE, db_column="credits_available",
                                    related_name="max_crd")
    registration_time = models.DateTimeField(auto_now=True)




from django.contrib import admin
from .models import *


# Register your models here.
class MajorAdmin(admin.ModelAdmin):
    list_display = ['num', 'name']


class StudentAdmin(admin.ModelAdmin):
    list_display = ['std_id', 'major', 'grade', 'credits_available']


class ProfessorAdmin(admin.ModelAdmin):
    list_display = ['prof_id', 'prof_name', 'prof_major']


class CourseAdmin(admin.ModelAdmin):
    list_display = ['code', 'name', 'credit', 'professor', 'classroom', 'weekday', 'start_time', 'finish_time']


admin.site.register(Major, MajorAdmin)
admin.site.register(Student, StudentAdmin)
admin.site.register(Professor, ProfessorAdmin)
admin.site.register(Course, CourseAdmin)
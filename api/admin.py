from django.contrib import admin
from .models import *


# Register your models here.

class UserAdmin(admin.ModelAdmin):
    list_display = ['id', 'email']


class MajorAdmin(admin.ModelAdmin):
    list_display = ['num', 'name']


class StudentAdmin(admin.ModelAdmin):
    list_display = ['std_id', 'major', 'grade', 'credits_available']


class ProfessorAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'major']


class CourseAdmin(admin.ModelAdmin):
    list_display = ['code', 'name', 'credit', 'professor', 'classroom', 'weekday', 'start_time', 'finish_time']


class BasketAdmin(admin.ModelAdmin):
    list_display = ['course', 'student']


class RegAdmin(admin.ModelAdmin):
    list_display = ['course', 'student', 'succeed_at']


admin.site.register(User, UserAdmin)
admin.site.register(Major, MajorAdmin)
admin.site.register(Student, StudentAdmin)
admin.site.register(Professor, ProfessorAdmin)
admin.site.register(Course, CourseAdmin)
admin.site.register(Basket, BasketAdmin)
admin.site.register(Registration, RegAdmin)
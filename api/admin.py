from django.contrib import admin
from .models import *
# Register your models here.


class BranchAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'location']


class ScreenAdmin(admin.ModelAdmin):
    list_display = ['name', 'branch']


class MovieAdmin(admin.ModelAdmin):
    list_display = ['title', 'genre']


class ScheduleAdmin(admin.ModelAdmin):
    list_display = ['start_time', 'finish_time', 'movie', 'branch', 'screen']


admin.site.register(Branch, BranchAdmin)
admin.site.register(Screen, ScreenAdmin)
admin.site.register(Movie, MovieAdmin)
admin.site.register(Schedule, ScheduleAdmin)


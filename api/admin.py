from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .models import User, Movie, Review, Booking, TimeTable, Genre, Director


class CustomUserAdmin(UserAdmin):
    # fieldsets : 관리자 리스트 화면에서 출력될 폼 설정 부분
    UserAdmin.fieldsets[1][1]['fields'] += ('gender', 'phone', 'wish_list')
    # add_fieldsets : User 객체 추가 화면에 출력될 입력 폼 설정 부분
    UserAdmin.add_fieldsets += (
        ('Additional Info', {'fields': ('gender', 'phone')})
    )


class GenresInline(admin.TabularInline):
    model = Genre
    extra = 2


class MovieAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {'fields': ['title']}),
        ('Informations', {'fields': ['country', 'rel_day', 'poster']}),
        (None, {'fields': ['is_on_now']}),
    ]
    inlines = [GenresInline]
    list_display = ('title', 'country', 'rel_day', 'is_on_now')


class TimeTableAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {'fields': ['movie', 'start_time', 'end_time']}),
    ]
    list_display = ('movie', 'start_time', 'end_time')


class ReviewAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {'fields': ['user', 'movie', 'rate', 'comment']}),
    ]
    list_display = ('user', 'movie', 'rate', 'comment')


class BookingAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {'fields': ['user', 'movie', 'movie_time', 'num_people', 'booking_time']}),
    ]
    list_display = ('user', 'movie', 'movie_time', 'num_people')


admin.site.register(User, CustomUserAdmin)
admin.site.register(Movie, MovieAdmin)
admin.site.register(Review, ReviewAdmin)
admin.site.register(Booking, BookingAdmin)
admin.site.register(TimeTable, TimeTableAdmin)

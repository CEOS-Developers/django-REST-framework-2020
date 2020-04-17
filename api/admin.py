from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .models import User, Movie, Review, Booking, TimeTable, Genre, Director, Country


class CustomUserAdmin(UserAdmin):
    # fieldsets : 관리자 리스트 화면에서 출력될 폼 설정 부분
    UserAdmin.fieldsets[1][1]['fields'] += ('gender', 'phone', 'wish_list')
    # add_fieldsets : User 객체 추가 화면에 출력될 입력 폼 설정 부분
    UserAdmin.add_fieldsets += (
        ('Additional Info', {'fields': ('gender', 'phone', 'wish_list')}),
    )


admin.site.register(User, CustomUserAdmin)
admin.site.register(Movie)
admin.site.register(Genre)
admin.site.register(Review)
admin.site.register(Booking)
admin.site.register(TimeTable)
admin.site.register(Director)
admin.site.register(Country)

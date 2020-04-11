from django.contrib import admin
from .models import MyUser


#admin.site.register(User)
@admin.register(MyUser)
class MyUserAdmin(admin.ModelAdmin):
    pass


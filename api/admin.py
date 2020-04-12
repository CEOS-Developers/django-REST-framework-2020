from django.contrib import admin
# from .models import MyUser
from . import models


# admin.site.register(User)
@admin.register(models.MyUser)
class MyUserAdmin(admin.ModelAdmin):
    pass


@admin.register(models.Product)
class ProductAdmin(admin.ModelAdmin):
    pass


@admin.register(models.Order)
class OrderAdmin(admin.ModelAdmin):
    pass


@admin.register(models.Manufacturer)
class ManufacturerAdmin(admin.ModelAdmin):
    pass


@admin.register(models.Delivery)
class DeliveryAdmin(admin.ModelAdmin):
    pass


@admin.register(models.Review)
class ReviewAdmin(admin.ModelAdmin):
    pass

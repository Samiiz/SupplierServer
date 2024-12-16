from django.contrib import admin

from account.models import Order, Product, User


# Register your models here.
@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    pass


@admin.register(Product)
class ProfileAdmin(admin.ModelAdmin):
    pass


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    pass

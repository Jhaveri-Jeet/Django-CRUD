from django.contrib import admin
from .models import UserDetails

# Register your models here.


class AdminUserDetails(admin.ModelAdmin):
    list_display = ("name", "email", "password", "image")
    search_fields = ("name", "email", "password")


admin.site.register(UserDetails, AdminUserDetails)
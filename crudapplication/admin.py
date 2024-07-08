from django.contrib import admin
from .models import UserDetails

class AdminPaneDisplayUserDetails(admin.ModelAdmin):
    list_display = ('name', 'email', 'password', 'image')
    search_fields = ('name', 'email', 'password', 'image')

admin.site.register(UserDetails, AdminPaneDisplayUserDetails)
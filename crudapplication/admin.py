from django.contrib import admin
from .models import *

class AdminPaneDisplayUserDetails(admin.ModelAdmin):
    list_display = ('name', 'email', 'password', 'image')
    search_fields = ('name', 'email', 'password', 'image')

admin.site.register(UserDetails, AdminPaneDisplayUserDetails)
admin.site.register(UserMoreDetails)
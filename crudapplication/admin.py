from django.contrib import admin
from .models import *

class AdminPaneDisplayUserDetails(admin.ModelAdmin):
    list_display = ('name', 'email', 'password', 'image')
    search_fields = ('name', 'email', 'password', 'image')

class AdminPanelDisplayProduct(admin.ModelAdmin):
    list_display = ('name', 'description')
    search_fields = ('name', 'description')

admin.site.register(UserDetails, AdminPaneDisplayUserDetails)
admin.site.register(UserMoreDetails)
admin.site.register(Product, AdminPanelDisplayProduct)
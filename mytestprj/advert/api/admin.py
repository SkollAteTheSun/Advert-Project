from django.contrib import admin

from .models import *

'''
class CustomUserAdmin(User):
    fieldsets = (
        ('Personal info', {'fields': ('username', 'password', 'name', 'email', 'first_name', 'last_name', 'is_active', 'is_staff', 'is_superuser', 'last_login', 'date_joined')}),
    )



admin.site.register(CustomUserAdmin)
'''
admin.site.register(Category)
admin.site.register(AdvertCategory)
admin.site.register(Advert)
admin.site.register(Proposal)

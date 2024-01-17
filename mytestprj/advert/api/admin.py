from django.contrib import admin

from .models import *

class AdvertCategoryInline(admin.StackedInline):
    model = AdvertCategory
    extra = 1

class AdvertAdmin(admin.ModelAdmin):
    inlines = [AdvertCategoryInline]


admin.site.register(Category)
admin.site.register(AdvertCategory)
admin.site.register(Advert, AdvertAdmin)
admin.site.register(Proposal)

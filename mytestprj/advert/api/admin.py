from django.contrib import admin

from .models import *

class AdvertCategoryInline(admin.StackedInline):
    model = AdvertCategory
    extra = 1

class AdvertAdmin(admin.ModelAdmin):
    inlines = [AdvertCategoryInline]
    actions = ['publish_adverts', 'hide_adverts']

    def publish_adverts(modeladmin, request, queryset):
        queryset.update(published=True)

    publish_adverts.short_description = "Опубликовать выбранные объявления"

    def hide_adverts(modeladmin, request, queryset):
        queryset.update(published=False)

    hide_adverts.short_description = "Скрыть выбранные объявления"


admin.site.register(Category)
admin.site.register(AdvertCategory)
admin.site.register(Advert, AdvertAdmin)
admin.site.register(Proposal)

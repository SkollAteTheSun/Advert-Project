from django.urls import path, reverse

from django.contrib import admin
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.contrib import messages

from .forms import *
from .views import *

class AdvertAdminForm(forms.ModelForm):
    csv_file = forms.FileField(label='CSV файл')

class AdvertCategoryInline(admin.StackedInline):
    form = AdvertAdminForm
    model = AdvertCategory
    extra = 1

class AdvertImportAdmin(admin.ModelAdmin):
    list_display = ('csv_file', 'date_added')

class AdvertAdmin(admin.ModelAdmin):
    form = AdvertAdminForm
    inlines = [AdvertCategoryInline]
    actions = ['publish_adverts', 'hide_adverts', 'import_csv']

    def publish_adverts(modeladmin, request, queryset):
        queryset.update(published=True)

    publish_adverts.short_description = "Опубликовать выбранные объявления"

    def hide_adverts(modeladmin, request, queryset):
        queryset.update(published=False)

    hide_adverts.short_description = "Скрыть выбранные объявления"

    def get_urls(self):
        urls = super().get_urls()
        custom_urls = [
            path('import-csv/', self.import_csv),
        ]
        return custom_urls + urls

    def import_csv(self, request):
        if request.method == "POST":
            form = CSVUploadForm(request.POST, request.FILES)
            if form.is_valid():
                csv_file = form.cleaned_data['csv_file']
                try:
                    decoded_file = csv_file.read().decode('utf-8').splitlines()
                    reader = csv.DictReader(decoded_file)
                    for row in reader:
                        try:
                            self.create_advert_from_csv(row)
                        except Exception as e:
                            logging.error(f'Error while importing advert from CSV: {str(e)}')

                    self.message_user(request, "Объявления успешно импортированы", level=messages.SUCCESS)
                    return HttpResponseRedirect("")
                except Exception as e:
                    logging.error(f'Error during CSV import: {str(e)}')
                    self.message_user(request, f'Ошибка при импорте CSV: {str(e)}', level=messages.ERROR)
                    return HttpResponseRedirect("")

                self.message_user(request, "Объявления успешно импортированы")
                return HttpResponseRedirect("..")
        else:
            form = CSVUploadForm()

        payload = {"form": form}
        return render( request, "admin/import_csv.html", payload)

    def create_advert_from_csv(self, csv_row):
        name = csv_row.get('name')
        description = csv_row.get('description')
        photo_path = csv_row.get('photo_path')
        published = csv_row.get('published')
        main_category_name = csv_row.get('main_category_name')

        advert = Advert(
            name=name,
            description=description,
            published=published,
        )

        print(main_category_name)

        user = User.objects.first()
        advert.user = user

        if photo_path:
            photo_path = os.path.join('media', 'avatars', csv_row.get('photo_path'))
            with open(photo_path, 'rb') as photo_file:
                advert.photo.save(photo_path, File(photo_file))
        else:
            logging.error(f'Photo path: {str(photo_path)}')

        advert.save()

        if main_category_name:
            try:
                main_category_instance = Category.objects.get(name=main_category_name)
                AdvertCategory.objects.create(advert=advert, category=main_category_instance, is_main=True)
            except Exception as e:
                logging.error(f'Error creating AdvertCategory: {str(e)}')

        return advert



admin.site.register(Category)
admin.site.register(AdvertCategory)
admin.site.register(Advert, AdvertAdmin)
admin.site.register(AdvertImport, AdvertImportAdmin)
admin.site.register(Proposal)

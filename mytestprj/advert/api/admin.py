from django.contrib import admin

from .forms import *
from .views import *

class AdvertAdminForm(forms.ModelForm):
    csv_file = forms.FileField(label='CSV файл')

    def clean_csv_file(self):
        csv_file = self.cleaned_data['csv_file']
        # Добавьте здесь логику валидации для CSV файла, если необходимо
        return csv_file
class AdvertCategoryInline(admin.StackedInline):
    form = AdvertAdminForm
    model = AdvertCategory
    extra = 1

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

    # def import_csv(self, request, csv_file):
    #     import_csv_view = ImportCSVView()
    #     import_csv_view.import_adverts_from_csv(csv_file)

    def import_csv(self, request, queryset):
        csv_file = request.FILES.get('csv_file')
        if csv_file:
            decoded_file = csv_file.read().decode('utf-8').splitlines()
            reader = csv.DictReader(decoded_file)
            for row in reader:
                try:
                    self.create_advert_from_csv(row)
                except Exception as e:
                    logging.error(f'Error while importing advert from CSV: {str(e)}')

            self.message_user(request, 'CSV файл успешно импортирован')

        else:
            self.message_user(request, 'Не выбран CSV файл для импорта', level='error')

    import_csv.short_description = 'Импорт объявлений из CSV'

admin.site.register(Category)
admin.site.register(AdvertCategory)
admin.site.register(Advert, AdvertAdmin)
admin.site.register(Proposal)

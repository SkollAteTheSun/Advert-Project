
from django import forms

from .models import *


class CSVUploadForm(forms.Form):
    class Meta:
        model = Advert
        fields = ('csv_file',)

    csv_file = forms.FileField(label="Выберите CSV файл")


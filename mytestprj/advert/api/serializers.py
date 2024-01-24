import logging
import os

from django.db.models import Max
from rest_framework import serializers
from .models import *


class CategorySerializer(serializers.ModelSerializer):

    class Meta:
        model = Category
        fields = ['name']


class ProposalSerializer(serializers.ModelSerializer):
    advert_info = serializers.SerializerMethodField()
    def get_advert_info(self, obj):
        return {
            'num_proposals': Proposal.objects.filter(advert=obj.advert).count(),
            'max_reward': Proposal.objects.filter(advert=obj.advert).aggregate(Max('reward'))['reward__max']
        }

    class Meta:
        model = Proposal
        fields = ['user', 'advert', 'reward', 'comment', 'accepted', 'advert_info']

class AdvertSerializer(serializers.ModelSerializer):
    class Meta:
        model = Advert
        fields = ['user', 'categories', 'name', 'description', 'photo', 'published']

    # @classmethod
    # def create_from_csv(cls, csv_row):
    #     # Извлеките данные из строки CSV
    #     name = csv_row.get('name')
    #     description = csv_row.get('description')
    #     photo_path = csv_row.get('photo_path')  # Подстройте под ваши столбцы CSV
    #     published = csv_row.get('published')
    #     main_category_name = csv_row.get('main_category_name')
    #
    #     # Создайте объект Advert
    #     advert = cls.Meta.model(
    #         name=name,
    #         description=description,
    #         published=published,
    #     )
    #
    #
    #     # Установите пользователя (возможно, вам нужно будет это настроить в соответствии с вашей логикой приложения)
    #     user = User.objects.first()  # Замените на вашу логику получения пользователя
    #     advert.user = user
    #
    #     print(photo_path)
    #
    #     if photo_path:
    #         photo_path = os.path.abspath(photo_path)
    #         # ...
    #         with open(photo_path, 'rb') as photo_file:
    #             advert.photo.save(photo_path, File(photo_file))
    #     else:
    #         logging.error(f'Photo path: {str(photo_path)}')
    #         # Обработка случая, когда photo_path отсутствует или пуст
    #         print("Путь к фото отсутствует в CSV.")
    #         print(photo_path)
    #
    #     # Сохраните объект Advert
    #     advert.save()
    #
    #     # Установите основную категорию
    #     if main_category_name:
    #         main_category = Category.objects.get(name=main_category_name)
    #         AdvertCategory.objects.create(advert=advert, category=main_category, is_main=True)
    #
    #     return advert
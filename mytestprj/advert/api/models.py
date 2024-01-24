from django.db import models

from django.contrib.auth.models import User
from django.core.files import File
import csv

class Category(models.Model):

    name = models.CharField(max_length=31, unique=True, verbose_name="Название категории")
    def __str__(self):
        return str(self.name)

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'


class PublishedAdvertManager(models.Manager):
    def published(self):
        return super().get_queryset().filter(published=True)

class Advert(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='adverts', verbose_name="Автор объявления")
    categories = models.ManyToManyField(Category, through='AdvertCategory', related_name='adverts',
                                        verbose_name="Категории")
    name = models.CharField(max_length=60, verbose_name="Название объявления")
    description = models.TextField(verbose_name="Описание")
    photo = models.ImageField(upload_to='avatars', verbose_name="Фото вещи")
    published = models.BooleanField(default=True, verbose_name="Опубликовано")

    #published_objects = PublishedAdvertManager()
    objects = PublishedAdvertManager()

    def __str__(self):
        return str(self.name)

    class Meta:
        verbose_name = 'Объявление'
        verbose_name_plural = 'Объявления'

class AdvertCategory(models.Model):
    advert = models.ForeignKey(Advert, on_delete=models.CASCADE, related_name='advert_categories', verbose_name="Объявление")
    category = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name="Категория вещи")
    is_main = models.BooleanField(default=False, verbose_name="Основная категория")

    def __str__(self):
        return f"{self.advert} - {self.category}"

    class Meta:
        verbose_name = 'Категория объявления'
        verbose_name_plural = 'Категории объявлений'
        unique_together = ('advert', 'is_main')


class Proposal(models.Model):

    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='proposals', verbose_name="Автор заявки")
    advert = models.ForeignKey(Advert, on_delete=models.CASCADE,related_name='proposals', verbose_name="Объявление")
    reward = models.IntegerField(blank=True, null=True, verbose_name="Денежное вознаграждение")
    comment = models.CharField(max_length= 120, blank=True, null=True, verbose_name="Комментарий к заявке")
    accepted = models.BooleanField(default=False, verbose_name="Принята автором объявления")

    def __str__(self):
        return str(self.advert)

    class Meta:
        verbose_name = 'Заявка'
        verbose_name_plural = 'Заявки'


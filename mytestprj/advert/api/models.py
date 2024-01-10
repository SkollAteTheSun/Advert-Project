from django.db import models

from authentication.models import CustomUser

class Category(models.Model):

    #Модель Категории
    name = models.CharField(max_length=31, unique=True, verbose_name="Название категории")

    def __str__(self):
        return str(self.name)

    class Meta:
        verbose_name_plural = 'Categories'


class Advert(models.Model):

    #Модель Объявления
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='advert', verbose_name="Автор объявления")
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='advert', verbose_name="Категория вещи")
    name = models.CharField(max_length=60, verbose_name="Название объявления")
    description = models.TextField(verbose_name="Описание")
    photo = models.ImageField(upload_to='avatars', verbose_name="Фото вещи")

    def __str__(self):
        return str(self.id)


class Proposal(models.Model):

    #Модель Заявки
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='proposal', verbose_name="Автор заявки")
    advert = models.ForeignKey(Advert, on_delete=models.CASCADE,related_name='proposal', verbose_name="Объявление")
    reward = models.IntegerField(blank=True, null=True, verbose_name="Денежное вознаграждение")
    comment = models.CharField(max_length= 120, blank=True, null=True, verbose_name="Комментарий к заявке")
    accepted = models.BooleanField(default=False, verbose_name="Принята автором объявления")

    def __str__(self):
        return str(self.id)


'''
class Category(models.Model):
    """
    Модель Категории
    """
    name = models.CharField(max_length=31, unique=True, verbose_name="Название категории")

    def __str__(self):
        return str(self.name)

    class Meta:
        verbose_name_plural = 'Categories'


class Advert(models.Model):
    """
    Модель Объявления
    """

    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, verbose_name="Автор объявления")
    category = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name="Категория вещи")
    name = models.CharField(max_length=63, verbose_name="Название объявления")
    description = models.CharField(max_length=127, verbose_name="Описание")
    photo = models.ImageField(upload_to='avatars', verbose_name="Фото вещи")

    def __str__(self):
        return str(self.id)


class Proposal(models.Model):
    """
    Модель Заявки
    """

    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, verbose_name="Автор заявки")
    advert = models.ForeignKey(Advert, on_delete=models.CASCADE, verbose_name="Объявление")
    reward = models.IntegerField(blank=True, null=True, verbose_name="Денежное вознаграждение")
    comment = models.CharField(max_length=127, blank=True, null=True, verbose_name="Комментарий к заявке")
    accepted = models.BooleanField(default=False, verbose_name="Принята автором объявления")

    def __str__(self):
        return str(self.id)
'''

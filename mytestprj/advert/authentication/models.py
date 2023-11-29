from django.db import models
from django.contrib.auth.models import AbstractUser


class CustomUser(AbstractUser):
    """
    Модель Пользователь
    """
    username = models.CharField(max_length=17, unique=True)
    password = models.TextField(max_length=50)
    first_name = models.TextField(max_length=50)
    last_name = models.TextField(max_length=50)

    def __str__(self):
        return str(self.id)

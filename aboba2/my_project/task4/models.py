
from django.db import models


class Game(models.Model):
    name = models.CharField(max_length=100, unique=True)  # Название игры
    description = models.TextField()  # Описание игры
    price = models.DecimalField(max_digits=10, decimal_places=2)  # Стоимость игры

    def __str__(self):
        return self.name  # Возвращает название игры в качестве строки


class Buyer(models.Model):
    name = models.CharField(max_length=100, unique=True)  # Имя покупателя
    email = models.EmailField(unique=True)  # Email покупателя

    def __str__(self):
        return self.name  # Возвращает имя покупателя в качестве строки

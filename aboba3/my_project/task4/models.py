from django.db import models

class Publisher(models.Model):
    name = models.CharField(max_length=255)
    country = models.CharField(max_length=100)

    class Meta:
        db_table = 'publisher'  

    def __str__(self):
        return self.name

class Developer(models.Model):
    name = models.CharField(max_length=255)
    founded_year = models.IntegerField()
    headquarters = models.CharField(max_length=100)

    class Meta:
        db_table = 'developer'
    def __str__(self):
        return self.name

class Game(models.Model):
    name = models.CharField(max_length=100, unique=True)  # Название игры
    description = models.TextField()  # Описание игры
    price = models.DecimalField(max_digits=10, decimal_places=2)  # Стоимость игры
    publisher = models.ForeignKey(Publisher, on_delete=models.CASCADE, related_name='games', null=True, blank=True)
    developer = models.ForeignKey(Developer, on_delete=models.CASCADE, related_name='games', null=True, blank=True)

    class Meta:
        db_table = 'task4_game'

    def __str__(self):
        return self.name  # Возвращает название игры в качестве строки



class Buyer(models.Model):
    name = models.CharField(max_length=100, unique=True)  # Имя покупателя
    email = models.EmailField(unique=True)  # Email покупателя

    def __str__(self):
        return self.name  # Возвращает имя покупателя в качестве строки

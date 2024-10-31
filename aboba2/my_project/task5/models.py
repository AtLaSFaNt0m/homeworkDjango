from django.db import models

class Buyer(models.Model):
    name = models.CharField(max_length=100, unique=True)  # Имя покупателя должно быть уникальным
    email = models.EmailField(unique=True)  # Email также должен быть уникальным

    def __str__(self):
        return self.name
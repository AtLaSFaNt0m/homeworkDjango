from django.contrib import admin
from .models import Game, Buyer

# Регистрация модели Game в админке
@admin.register(Game)
class GameAdmin(admin.ModelAdmin):
    list_display = ('name', 'price')  # Поля, отображаемые в списке игр
    search_fields = ('name',)  # Поля, по которым можно осуществлять поиск

# Регистрация модели Buyer в админке
@admin.register(Buyer)
class BuyerAdmin(admin.ModelAdmin):
    list_display = ('name', 'email')  # Поля, отображаемые в списке покупателей
    search_fields = ('name',)  # Поля, по которым можно осуществлять поиск

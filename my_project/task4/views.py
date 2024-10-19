from django.shortcuts import render
from .models import Game
# Представление для главной страницы
def main_view(request):
    return render(request, 'fourth_task/main.html')

# Представление для магазина (добавлен список игр)
def shop_view(request):
    games = Game.objects.all()  # Извлекаем все игры
    return render(request, 'fourth_task/shop.html', {'games': games}) 
# Представление для корзины (показывает список игр, добавленных в корзину)
def cart_view(request):
    cart = request.session.get('cart', [])
    context = {'cart': cart}
    return render(request, 'fourth_task/cart.html', context)

# Представление с контекстом для списка игр (опционально)
def games_view(request):
    games = Game.objects.all()  # Получаем все записи из таблицы Game
    return render(request, 'fourth_task/games.html', {'games': games}) 

# Добавить игру в корзину
def add_to_cart(request, game_name):
    # Получаем текущую корзину из сессии или создаём новую как список
    cart = request.session.get('cart', [])

    # Добавляем игру в корзину
    cart.append(game_name)

    # Сохраняем обновлённую корзину в сессии
    request.session['cart'] = cart

    return redirect('/shop/')

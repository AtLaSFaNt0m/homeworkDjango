from django.shortcuts import render, redirect, get_object_or_404
from .models import Game

# Представление для главной страницы
def main_view(request):
    return render(request, 'fourth_task/main.html')

# Представление для оформления заказа
def checkout_view(request):
    # Здесь может быть логика оформления заказа
    return render(request, 'fourth_task/checkout.html')  # Убедитесь, что у вас есть шаблон для этого

# Представление для магазина (добавлен список игр)
def shop_view(request):
    games = Game.objects.all()  
    return render(request, 'fourth_task/shop.html', {'games': games}) 

# Представление для корзины (показывает список игр, добавленных в корзину)
def cart_view(request):
    cart = request.session.get('cart', [])
    context = {'cart': cart}
    return render(request, 'fourth_task/cart.html', context)

# Представление с контекстом для списка игр
def games_view(request):
    games = Game.objects.all()  # Получаем все записи из таблицы Game
    return render(request, 'fourth_task/games.html', {'games': games}) 

# Добавить игру в корзину
def add_to_cart(request, game_name):
    # Получаем текущую корзину из сессии или создаём новую как список
    cart = request.session.get('cart', [])

    # Получаем игру по имени
    game = get_object_or_404(Game, name=game_name)
    
    # Добавляем имя игры в корзину
    cart.append(game.name)

    # Сохраняем обновлённую корзину в сессии
    request.session['cart'] = cart

    # Возврат на страницу магазина (или другую страницу)
    return redirect('shop')
from django.shortcuts import render, redirect
from task5.models import Buyer

def register_view(request):
    error_message = None
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')

        # Проверка, существует ли уже пользователь с таким именем
        if Buyer.objects.filter(name=username).exists():
            error_message = "Такой пользователь уже существует."
        elif not email:  # Проверка, что email не пустой
            error_message = "Email не может быть пустым."
        else:
            # Создание нового пользователя
            Buyer.objects.create(name=username, email=email)
            return redirect('main')  # Перенаправление на главную страницу после успешной регистрации

    return render(request, 'fifth_task/registration_page.html', {'error_message': error_message})
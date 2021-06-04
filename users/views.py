from django.shortcuts import render


def login(request):
    context = {
        'title': 'GeekShop - авторизация'
    }
    return render(request, 'users/login.html', context)


def register(request):
    context = {
        'title': 'GeekShop - регистрация'
    }
    return render(request, 'users/register.html',context)

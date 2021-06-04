from django.shortcuts import render
from users.forms import UserLoginForm


def login(request):
    form = UserLoginForm()
    context = {
        'title': 'GeekShop - авторизация',
        'form': form
    }
    return render(request, 'users/login.html', context)


def register(request):
    context = {
        'title': 'GeekShop - регистрация'
    }
    return render(request, 'users/register.html',context)

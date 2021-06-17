from django.contrib import messages
from django.shortcuts import render, HttpResponseRedirect
from django.urls import reverse

from users.models import User
from admins.forms import UserAdminRegisterForm, UserAdminProfileForm


def index(request):
    context = {
        'title': 'GeekShop - Админ'
    }
    return render(request, 'admins/admin.html', context)


def admin_users(request):
    context = {
        'title': 'GeekShop - Админ | Пользователи',
        'users': User.objects.all()
    }
    return render(request, 'admins/admin-users-read.html', context)


def admin_users_create(request):
    if request.method == 'POST':
        form = UserAdminRegisterForm(data=request.POST, files=request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('admins:admin_users'))
    else:
        form = UserAdminRegisterForm()
    context = {
        'title': 'GeekShop - Админ | Создание пользователя',
        'form': form
    }
    return render(request, 'admins/admin-users-create.html', context)


def admin_users_update(request, id):
    user = User.objects.get(id=id)
    if request.method == 'POST':
        form = UserAdminProfileForm(data=request.POST, files=request.FILES, instance=user)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('admins:admin_users'))
    else:
        form = UserAdminProfileForm(instance=user)
    content = {
        'title': f'GeekShop - Админ | Профиль {user.username}',
        'user': user,
        'form': form
    }
    return render(request, 'admins/admin-users-update-delete.html', content)


def admin_users_delete(request, id):
    pass

from django.contrib import messages
from django.contrib.auth.decorators import user_passes_test
from django.shortcuts import render, HttpResponseRedirect
from django.urls import reverse

from products.models import Product
from users.models import User
from admins.forms import UserAdminRegisterForm, UserAdminProfileForm, ProductAdminCreationForm


@user_passes_test(lambda u: u.is_superuser)
def index(request):
    context = {
        'title': 'GeekShop - Админ'
    }
    return render(request, 'admins/admin.html', context)


@user_passes_test(lambda u: u.is_superuser)
def admin_users(request):
    context = {
        'title': 'GeekShop - Админ | Пользователи',
        'users': User.objects.all()
    }
    return render(request, 'admins/admin-users-read.html', context)


@user_passes_test(lambda u: u.is_superuser)
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


@user_passes_test(lambda u: u.is_superuser)
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


@user_passes_test(lambda u: u.is_superuser)
def admin_users_delete(request, id):
    user = User.objects.get(id=id)
    user.is_active = False
    user.save()
    return HttpResponseRedirect(reverse('admins:admin_users'))


@user_passes_test(lambda u: u.is_superuser)
def admin_users_restore(request, id):
    user = User.objects.get(id=id)
    user.is_active = True
    user.save()
    return HttpResponseRedirect(reverse('admins:admin_users'))


@user_passes_test(lambda u: u.is_superuser)
def admin_products(request):
    context = {
        'title': 'GeekShop - Админ | Продукты',
        'products': Product.objects.all()
    }
    return render(request, 'admins/admin-products-read.html', context)


@user_passes_test(lambda u: u.is_superuser)
def admin_products_create(request):
    if request.method == 'POST':
        form = ProductAdminCreationForm(data=request.POST, files=request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('admins:admin_products'))
    else:
        form = ProductAdminCreationForm()
    context = {
        'title': 'GeekShop - Админ | Создание пользователя',
        'form': form
    }
    return render(request, 'admins/admin-products-create.html', context)


@user_passes_test(lambda u: u.is_superuser)
def admin_products_update(request, id):
    pass


@user_passes_test(lambda u: u.is_superuser)
def admin_products_delete(request, id):
    pass


@user_passes_test(lambda u: u.is_superuser)
def admin_products_restore(request, id):
    pass

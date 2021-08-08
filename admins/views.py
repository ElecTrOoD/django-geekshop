from django.contrib.auth.decorators import user_passes_test
from django.shortcuts import HttpResponseRedirect
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.views.generic.base import TemplateView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.list import ListView

from admins.forms import UserAdminRegisterForm, UserAdminProfileForm, ProductAdminForm
from orders.models import Order
from products.models import Product
from users.models import User


class AdminIndexView(TemplateView):
    template_name = 'admins/admin.html'
    extra_context = {'title': 'GeekShop - Админ'}

    @method_decorator(user_passes_test(lambda u: u.is_superuser))
    def dispatch(self, request, *args, **kwargs):
        return super(AdminIndexView, self).dispatch(request, *args, **kwargs)


class AdminUserListView(ListView):
    model = User
    template_name = 'admins/admin-users-read.html'
    extra_context = {'title': 'GeekShop - Админ | Пользователи'}

    @method_decorator(user_passes_test(lambda u: u.is_superuser))
    def dispatch(self, request, *args, **kwargs):
        return super(AdminUserListView, self).dispatch(request, *args, **kwargs)


class AdminUserCreateView(CreateView):
    model = User
    template_name = 'admins/admin-users-create.html'
    form_class = UserAdminRegisterForm
    success_url = reverse_lazy('admins:admin_users')
    extra_context = {'title': 'GeekShop - Админ | Создание пользователя'}

    @method_decorator(user_passes_test(lambda u: u.is_superuser))
    def dispatch(self, request, *args, **kwargs):
        return super(AdminUserCreateView, self).dispatch(request, *args, **kwargs)


class AdminUserUpdateView(UpdateView):
    model = User
    template_name = 'admins/admin-users-update-delete.html'
    form_class = UserAdminProfileForm
    success_url = reverse_lazy('admins:admin_users')
    extra_context = {'title': 'GeekShop - Админ | Профиль'}

    @method_decorator(user_passes_test(lambda u: u.is_superuser))
    def dispatch(self, request, *args, **kwargs):
        return super(AdminUserUpdateView, self).dispatch(request, *args, **kwargs)


class AdminUserDeleteView(DeleteView):
    model = User
    template_name = 'admins/admin-users-update-delete.html'
    success_url = reverse_lazy('admins:admin_users')

    def delete(self, request, *args, **kwargs):
        self.object = self.get_object()
        if self.object.is_active:
            self.object.is_active = False
        else:
            self.object.is_active = True
        self.object.save()
        return HttpResponseRedirect(self.get_success_url())

    @method_decorator(user_passes_test(lambda u: u.is_superuser))
    def dispatch(self, request, *args, **kwargs):
        return super(AdminUserDeleteView, self).dispatch(request, *args, **kwargs)


class AdminUserCompleteDeleteView(DeleteView):
    model = User
    template_name = 'admins/admin-users-update-delete.html'
    success_url = reverse_lazy('admins:admin_users')

    @method_decorator(user_passes_test(lambda u: u.is_superuser))
    def dispatch(self, request, *args, **kwargs):
        return super(AdminUserCompleteDeleteView, self).dispatch(request, *args, **kwargs)


class AdminProductListView(ListView):
    model = Product
    template_name = 'admins/admin-products-read.html'
    extra_context = {'title': 'GeekShop - Админ | Продукты'}

    @method_decorator(user_passes_test(lambda u: u.is_superuser))
    def dispatch(self, request, *args, **kwargs):
        return super(AdminProductListView, self).dispatch(request, *args, **kwargs)


class AdminProductCreateView(CreateView):
    model = Product
    template_name = 'admins/admin-products-create.html'
    form_class = ProductAdminForm
    success_url = reverse_lazy('admins:admin_products')
    extra_context = {'title': 'GeekShop - Админ | Создание продукта'}

    @method_decorator(user_passes_test(lambda u: u.is_superuser))
    def dispatch(self, request, *args, **kwargs):
        return super(AdminProductCreateView, self).dispatch(request, *args, **kwargs)


class AdminProductUpdateView(UpdateView):
    model = Product
    template_name = 'admins/admin-products-update-delete.html'
    form_class = ProductAdminForm
    success_url = reverse_lazy('admins:admin_products')
    extra_context = {'title': 'GeekShop - Админ | Продукт'}

    @method_decorator(user_passes_test(lambda u: u.is_superuser))
    def dispatch(self, request, *args, **kwargs):
        return super(AdminProductUpdateView, self).dispatch(request, *args, **kwargs)


class AdminProductDeleteView(AdminUserDeleteView):
    model = Product
    template_name = 'admins/admin-products-update-delete.html'
    success_url = reverse_lazy('admins:admin_products')

    @method_decorator(user_passes_test(lambda u: u.is_superuser))
    def dispatch(self, request, *args, **kwargs):
        return super(AdminProductDeleteView, self).dispatch(request, *args, **kwargs)


class AdminProductCompleteDeleteView(DeleteView):
    model = Product
    template_name = 'admins/admin-products-update-delete.html'
    success_url = reverse_lazy('admins:admin_products')

    @method_decorator(user_passes_test(lambda u: u.is_superuser))
    def dispatch(self, request, *args, **kwargs):
        return super(AdminProductCompleteDeleteView, self).dispatch(request, *args, **kwargs)


class AdminOrderListView(ListView):
    model = Order
    template_name = 'admins/admin-orders-read.html'
    extra_context = {'title': 'GeekShop - Админ | Заказы'}

    @method_decorator(user_passes_test(lambda u: u.is_superuser))
    def dispatch(self, request, *args, **kwargs):
        return super(AdminOrderListView, self).dispatch(request, *args, **kwargs)


def update_order_status(request, pk):
    order = Order.objects.get(pk=pk)
    if not order.status == Order.CANCELED:
        STATUSES = {
            'FM': Order.PROCEED,
            'PRC': Order.DELIVERY,
            'DLV': Order.DONE,
        }
        order.status = STATUSES[order.status]
        order.save()
    return HttpResponseRedirect(reverse_lazy('admins:admin_orders'))


def cancel_order(request, pk):
    Order.objects.get(pk=pk).delete()
    return HttpResponseRedirect(reverse_lazy('admins:admin_orders'))

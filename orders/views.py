from django.db import transaction
from django.forms import inlineformset_factory
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404
from django.urls import reverse_lazy, reverse
from django.views.generic import ListView, CreateView, DeleteView, UpdateView, DetailView

from baskets.models import Basket
from orders.forms import OrderItemForm
from orders.models import Order, OrderItem


class OrderList(ListView):
    model = Order
    extra_context = {'title': 'Список заказов'}

    def get_queryset(self):
        return Order.objects.filter(user=self.request.user)


class OrderItemCreate(CreateView):
    model = Order
    fields = []
    success_url = reverse_lazy('orders:orders_list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        OrderFormset = inlineformset_factory(Order, OrderItem, form=OrderItemForm, extra=1)

        if self.request.method == 'POST':
            formset = OrderFormset(self.request.POST)
        else:
            basket_items = Basket.objects.filter(user=self.request.user)
            if basket_items.exists():
                OrderFormset = inlineformset_factory(Order, OrderItem, form=OrderItemForm, extra=basket_items.count())
                formset = OrderFormset()
                for num, form in enumerate(formset.forms):
                    form.initial['product'] = basket_items[num].product
                    form.initial['quantity'] = basket_items[num].quantity
            else:
                formset = OrderFormset()

        context['orderitems'] = formset
        context['title'] = 'Создание заказа'
        return context

    def form_valid(self, form):
        context = self.get_context_data()
        orderitems = context['orderitems']

        with transaction.atomic():
            user = self.request.user
            form.instance.user = user
            Basket.objects.filter(user=user).delete()
            self.object = form.save()
            if orderitems.is_valid():
                orderitems.instance = self.object
                orderitems.save()

        return super().form_valid(form)


class OrderItemRead(DetailView):
    model = Order
    extra_context = {'title': 'Детали заказа'}


class OrderItemUpdate(UpdateView):
    model = Order
    fields = []
    success_url = reverse_lazy('orders:orders_list')
    extra_context = {'title': 'Редактирование заказа'}

    def get_context_data(self, **kwargs):
        data = super().get_context_data(**kwargs)
        OrderFormset = inlineformset_factory(Order, OrderItem, form=OrderItemForm, extra=1)

        if self.request.method == 'POST':
            formset = OrderFormset(self.request.POST, instance=self.object)
        else:
            formset = OrderFormset(instance=self.object)

        data['orderitems'] = formset
        return data

    def form_valid(self, form):
        context = self.get_context_data()
        orderitems = context['orderitems']

        with transaction.atomic():
            form.instance.user = self.request.user
            self.object = form.save()
            if orderitems.is_valid():
                orderitems.instance = self.object
                orderitems.save()

        return super().form_valid(form)


class OrderItemDelete(DeleteView):
    model = Order
    success_url = reverse_lazy('orders:orders_list')
    extra_context = {'title': 'Удаление заказа'}


def confirm_order_forming(request, pk):
    order = get_object_or_404(Order, pk=pk)
    order.status = Order.PROCEED
    order.save()
    return HttpResponseRedirect(reverse('orders:orders_list'))

from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.shortcuts import HttpResponseRedirect
from django.template.loader import render_to_string

from baskets.models import Basket
from products.models import Product


@login_required
def add_to_basket(request, product_id, category_id=None):
    if request.is_ajax():
        product = Product.objects.get(id=product_id)
        baskets = Basket.objects.filter(user=request.user, product=product).select_related()

        if not baskets.exists():
            Basket.objects.create(user=request.user, product=product, quantity=1)
        else:
            basket = baskets.first()
            basket.quantity += 1
            basket.save()

        if category_id:
            products = Product.objects.filter(is_active=True, category_id=category_id).select_related()
        else:
            products = Product.objects.filter(is_active=True).select_related()
        context = {'object_list': products}
        result = render_to_string('products/products_list.html', context, request)
        return JsonResponse({'result': result})


@login_required
def remove_from_basket(request, id):
    Basket.objects.get(id=id).delete()
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))


@login_required()
def basket_edit(request, id, quantity):
    if request.is_ajax():
        basket = Basket.objects.get(id=id)
        if quantity > 0:
            if quantity > basket.quantity:
                basket.quantity = quantity
            elif quantity != basket.quantity:
                basket.quantity = quantity
            basket.save()
        else:
            basket.delete()
        baskets = Basket.objects.filter(user=request.user)
        context = {'baskets': baskets}
        result = render_to_string('baskets/baskets.html', context)
        return JsonResponse({'result': result})

from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.shortcuts import HttpResponseRedirect
from django.template.loader import render_to_string

from baskets.models import Basket
from products.models import Product


# @login_required
# def add_to_basket(request, product_id):
#     product = Product.objects.get(id=product_id)
#     baskets = Basket.objects.filter(user=request.user, product=product)
#
#     if not baskets.exists():
#         Basket.objects.create(user=request.user, product=product, quantity=1)
#         return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
#     else:
#         basket = baskets.first()
#         basket.quantity += 1
#         basket.save()
#         return HttpResponseRedirect(request.META.get('HTTP_REFERER'))

@login_required
def add_to_basket(request, product_id):
    if request.is_ajax():
        product = Product.objects.get(id=product_id)
        baskets = Basket.objects.filter(user=request.user, product=product)
        product.decrement_quantity()

        if not baskets.exists():
            Basket.objects.create(user=request.user, product=product, quantity=1)
        else:
            basket = baskets.first()
            basket.quantity += 1
            basket.save()

        products = Product.objects.filter(is_active=True)
        context = {'products': products}
        result = render_to_string('products/products_list.html', context)
        return JsonResponse({'result': result})


@login_required
def remove_from_basket(request, id):
    basket = Basket.objects.get(id=id)
    basket.product.set_quantity(basket.quantity)
    basket.delete()
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))


@login_required()
def basket_edit(request, id, quantity):
    if request.is_ajax():
        basket = Basket.objects.get(id=id)
        if quantity > 0:
            if basket.quantity > quantity:
                basket.product.increment_quantity()
            else:
                basket.product.decrement_quantity()
            basket.quantity = quantity
            basket.save()
        else:
            basket.delete()
        baskets = Basket.objects.filter(user=request.user)
        context = {'baskets': baskets}
        result = render_to_string('baskets/baskets.html', context)
        return JsonResponse({'result': result})

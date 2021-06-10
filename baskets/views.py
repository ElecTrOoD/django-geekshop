from django.contrib.auth.decorators import login_required
from django.shortcuts import HttpResponseRedirect

from baskets.models import Basket
from products.models import Product


@login_required
def add_to_basket(request, product_id):
    product = Product.objects.get(id=product_id)
    baskets = Basket.objects.filter(user=request.user, product=product)

    if not baskets.exists():
        Basket.objects.create(user=request.user, product=product, quantity=1)
        return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
    else:
        basket = baskets.first()
        basket.quantity += 1
        basket.save()
        return HttpResponseRedirect(request.META.get('HTTP_REFERER'))


@login_required
def remove_from_basket(request, id):
    basket = Basket.objects.get(id=id)
    if basket.quantity > 1:
        basket.quantity -= 1
        basket.save()
    else:
        basket.delete()
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))

from django.shortcuts import render

from products.models import Product


def index(request):
    context = {
        'title': 'GeekShop'
    }
    return render(request, 'products/index.html', context)


def products(request):
    goods = Product.objects.all()
    context = {
        'title': 'GeekShop - Каталог',
        'products': goods
    }
    return render(request, 'products/products.html', context)

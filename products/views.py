from django.shortcuts import render

from products.models import Product, ProductCategory


def index(request):
    context = {
        'title': 'GeekShop'
    }
    return render(request, 'products/index.html', context)


def products(request, category_id=None):
    if category_id:
        goods = Product.objects.filter(is_active=True, category_id=category_id)
    else:
        goods = Product.objects.filter(is_active=True)
    context = {
        'title': 'GeekShop - Каталог',
        'categories': ProductCategory.objects.all(),
        'products': goods
    }
    return render(request, 'products/products.html', context)

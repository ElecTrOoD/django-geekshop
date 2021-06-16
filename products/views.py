from django.shortcuts import render

from products.models import Product, ProductCategory


def index(request):
    context = {
        'title': 'GeekShop'
    }
    return render(request, 'products/index.html', context)


def products(request):
    goods = Product.objects.filter(is_active=True)
    categories = ProductCategory.objects.all()
    context = {
        'title': 'GeekShop - Каталог',
        'products': goods,
        'categories': categories
    }
    return render(request, 'products/products.html', context)

import json

from django.shortcuts import render

from geekshop.settings import BASE_DIR


def index(request):
    context = {
        'title': 'GeekShop'
    }
    return render(request, 'products/index.html', context)


def products(request):
    with open(BASE_DIR / 'products/fixtures/products.json', 'r', encoding='utf-8') as js:
        products_data = json.load(js)
    context = {
        'title': 'GeekShop - Каталог',
        'products': products_data
    }
    return render(request, 'products/products.html', context)

from django.shortcuts import render
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

from products.models import Product, ProductCategory


def index(request):
    context = {
        'title': 'GeekShop'
    }
    return render(request, 'products/index.html', context)


def products(request, category_id=None, page=1):
    if category_id:
        goods = Product.objects.filter(is_active=True, category_id=category_id)
    else:
        goods = Product.objects.filter(is_active=True)
    paginator = Paginator(goods, 3)
    try:
        products_paginator = paginator.page(page)
    except PageNotAnInteger:
        products_paginator = paginator.page(1)
    except EmptyPage:
        products_paginator = paginator.page(paginator.num_pages)

    context = {
        'title': 'GeekShop - Каталог',
        'categories': ProductCategory.objects.all(),
        'products': products_paginator
    }
    return render(request, 'products/products.html', context)

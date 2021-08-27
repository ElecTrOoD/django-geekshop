from django.conf import settings
from django.core.cache import cache
from django.views.generic import TemplateView
from django.views.generic.list import ListView

from products.models import Product, ProductCategory


def get_links_menu():
    if settings.LOW_CACHE:
        key = 'links_menu'
        links_menu = cache.get(key)
        if links_menu is None:
            links_menu = ProductCategory.objects.all()
            cache.set(key, links_menu)
        return links_menu
    else:
        return ProductCategory.objects.all()


def get_products():
    if settings.LOW_CACHE:
        key = 'products'
        products = cache.get(key)
        if products is None:
            products = Product.objects.filter(is_active=True)
            cache.set(key, products)
        return products
    else:
        return Product.objects.filter(is_active=True)


def get_products_by_category(category):
    category_id = ProductCategory.objects.get(name=category)
    if settings.LOW_CACHE:
        key = f'products_by_category_{category_id.id}'
        products = cache.get(key)
        if products is None:
            products = Product.objects.filter(category_id=category_id, is_active=True)
            cache.set(key, products)
        return products
    else:
        return Product.objects.filter(category_id=category_id, is_active=True)


class IndexView(TemplateView):
    template_name = 'products/index.html'
    extra_context = {'title': 'GeekShop'}


class ProductListView(ListView):
    model = Product
    template_name = 'products/products.html'
    paginate_by = 3
    extra_context = {
        'title': 'GeekShop - Каталог',
        'categories': get_links_menu(),
    }

    def get_queryset(self):
        if self.request.GET.get('filter'):
            category_name = self.request.GET.get('filter')
            new_queryset = get_products_by_category(category_name)
        else:
            new_queryset = Product.objects.filter(is_active=True)
        return new_queryset

    def get_context_data(self, **kwargs):
        context = super(ProductListView, self).get_context_data(**kwargs)
        context['filter'] = self.request.GET.get('filter')
        return context

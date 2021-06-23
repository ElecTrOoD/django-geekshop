from django.views.generic import TemplateView
from django.views.generic.list import ListView

from products.models import Product, ProductCategory


class IndexView(TemplateView):
    template_name = 'products/index.html'
    extra_context = {'title': 'GeekShop'}


class ProductListView(ListView):
    model = Product
    template_name = 'products/products.html'
    paginate_by = 3
    extra_context = {
        'title': 'GeekShop - Каталог',
        'categories': ProductCategory.objects.all(),
    }

    def get_queryset(self):
        if self.request.GET.get('filter'):
            category_name = self.request.GET.get('filter')
            new_queryset = Product.objects.filter(category_id=ProductCategory.objects.get(name=category_name),
                                                  is_active=True)
        else:
            new_queryset = Product.objects.filter(is_active=True)
        return new_queryset

    def get_context_data(self, **kwargs):
        context = super(ProductListView, self).get_context_data(**kwargs)
        context['filter'] = self.request.GET.get('filter')
        return context

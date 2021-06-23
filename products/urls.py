from django.urls import path

from products.views import ProductListView

app_name = 'products'

urlpatterns = [
    path('', ProductListView.as_view(), name='index'),
    path('page/<int:page>/', ProductListView.as_view(), name='page')
]

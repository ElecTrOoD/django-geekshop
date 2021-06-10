from django.urls import path

from baskets.views import add_to_basket

app_name = 'products'

urlpatterns = [
    path('add/<int:product_id>/', add_to_basket, name='add_to_basket')
]
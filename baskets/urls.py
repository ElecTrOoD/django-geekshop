from django.urls import path

from baskets.views import add_to_basket, remove_from_basket, basket_edit

app_name = 'products'

urlpatterns = [
    path('add/<int:product_id>/', add_to_basket, name='add_to_basket'),
    path('add/<int:product_id>/<int:category_id>/', add_to_basket, name='add_to_basket_category'),
    path('remove/<int:id>/', remove_from_basket, name='remove_from_basket'),
    path('edit/<int:id>/<int:quantity>/', basket_edit, name='basket_edit'),
]
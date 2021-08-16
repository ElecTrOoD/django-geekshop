from django.urls import path

from orders.views import OrderList, OrderItemCreate, OrderItemUpdate, OrderItemDelete, OrderItemRead, \
    confirm_order_forming, product_price

app_name = 'orders'

urlpatterns = [
    path('', OrderList.as_view(), name='orders_list'),
    path('create/', OrderItemCreate.as_view(), name='orders_create'),
    path('<pk>/', OrderItemRead.as_view(), name='orders_read'),
    path('update/<pk>/', OrderItemUpdate.as_view(), name='orders_update'),
    path('delete/<pk>/', OrderItemDelete.as_view(), name='orders_delete'),
    path('confirm/<pk>/', confirm_order_forming, name='orders_confirm'),
    path('product/<pk>/price/', product_price, name='product_price'),
]

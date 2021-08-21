from django.contrib.auth.decorators import login_required
from django.urls import path

from orders.views import OrderList, OrderItemCreate, OrderItemUpdate, OrderItemDelete, OrderItemRead, \
    confirm_order_forming, product_price

app_name = 'orders'

urlpatterns = [
    path('', login_required(OrderList.as_view()), name='orders_list'),
    path('create/', login_required(OrderItemCreate.as_view()), name='orders_create'),
    path('<pk>/', login_required(OrderItemRead.as_view()), name='orders_read'),
    path('update/<pk>/', login_required(OrderItemUpdate.as_view()), name='orders_update'),
    path('delete/<pk>/', login_required(OrderItemDelete.as_view()), name='orders_delete'),
    path('confirm/<pk>/', login_required(confirm_order_forming), name='orders_confirm'),
    path('product/<pk>/price/', login_required(product_price), name='product_price'),
]

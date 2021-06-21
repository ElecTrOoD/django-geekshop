from django.urls import path

from admins.views import IndexView, UserListView, UserCreateView, UserUpdateView, UserDeleteView, UserCompleteDeleteView, ProductListView, ProductCreateView, ProductUpdateView, ProductDeleteView, ProductCompleteDeleteView

app_name = 'admins'

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('users', UserListView.as_view(), name='admin_users'),
    path('users/create/', UserCreateView.as_view(), name='admin_users_create'),
    path('users/update/<int:pk>', UserUpdateView.as_view(), name='admin_users_update'),
    path('users/delete/<int:pk>', UserDeleteView.as_view(), name='admin_users_delete'),
    path('users/complete-delete/<int:pk>', UserCompleteDeleteView, name='admin_users_complete_delete'),
    path('products', ProductListView.as_view(), name='admin_products'),
    path('products/create/', ProductCreateView.as_view(), name='admin_products_create'),
    path('products/update/<int:pk>', ProductUpdateView.as_view(), name='admin_products_update'),
    path('products/delete/<int:pk>', ProductDeleteView.as_view(), name='admin_products_delete'),
    path('products/complete-delete/<int:pk>', ProductCompleteDeleteView.as_view(), name='admin_products_complete_delete'),
]

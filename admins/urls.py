from django.urls import path

from admins.views import AdminIndexView, AdminUserListView, AdminUserCreateView, AdminUserUpdateView, \
    AdminUserDeleteView, AdminUserCompleteDeleteView, AdminProductListView, AdminProductCreateView, \
    AdminProductUpdateView, AdminProductDeleteView, AdminProductCompleteDeleteView

app_name = 'admins'

urlpatterns = [
    path('', AdminIndexView.as_view(), name='index'),
    path('users', AdminUserListView.as_view(), name='admin_users'),
    path('users/create/', AdminUserCreateView.as_view(), name='admin_users_create'),
    path('users/update/<int:pk>', AdminUserUpdateView.as_view(), name='admin_users_update'),
    path('users/delete/<int:pk>', AdminUserDeleteView.as_view(), name='admin_users_delete'),
    path('users/complete-delete/<int:pk>', AdminUserCompleteDeleteView, name='admin_users_complete_delete'),
    path('products', AdminProductListView.as_view(), name='admin_products'),
    path('products/create/', AdminProductCreateView.as_view(), name='admin_products_create'),
    path('products/update/<int:pk>', AdminProductUpdateView.as_view(), name='admin_products_update'),
    path('products/delete/<int:pk>', AdminProductDeleteView.as_view(), name='admin_products_delete'),
    path('products/complete-delete/<int:pk>', AdminProductCompleteDeleteView.as_view(),
         name='admin_products_complete_delete'),
]

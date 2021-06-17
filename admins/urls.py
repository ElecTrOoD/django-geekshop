from django.urls import path

from admins.views import index, admin_users, admin_users_update, admin_users_create, admin_users_delete, \
    admin_users_complete_delete, admin_users_restore, admin_products, admin_products_create, admin_products_update, \
    admin_products_delete, admin_products_complete_delete, admin_products_restore

app_name = 'admins'

urlpatterns = [
    path('', index, name='index'),
    path('users', admin_users, name='admin_users'),
    path('users/create/', admin_users_create, name='admin_users_create'),
    path('users/update/<int:id>', admin_users_update, name='admin_users_update'),
    path('users/delete/<int:id>', admin_users_delete, name='admin_users_delete'),
    path('users/complete-delete/<int:id>', admin_users_complete_delete, name='admin_users_complete_delete'),
    path('users/restore/<int:id>', admin_users_restore, name='admin_users_restore'),
    path('products', admin_products, name='admin_products'),
    path('products/create/', admin_products_create, name='admin_products_create'),
    path('products/update/<int:id>', admin_products_update, name='admin_products_update'),
    path('products/delete/<int:id>', admin_products_delete, name='admin_products_delete'),
    path('products/complete-delete/<int:id>', admin_products_complete_delete, name='admin_products_complete_delete'),
    path('products/restore/<int:id>', admin_products_restore, name='admin_products_restore'),
]

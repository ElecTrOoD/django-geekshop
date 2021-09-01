from django.urls import path

from admins.views import AdminIndexView, AdminUserListView, AdminUserCreateView, AdminUserUpdateView, \
    AdminUserDeleteView, AdminUserCompleteDeleteView, AdminProductListView, AdminProductCreateView, \
    AdminProductUpdateView, AdminProductDeleteView, AdminProductCompleteDeleteView, AdminOrderListView, \
    AdminProductCategoryListView, AdminProductCategoryCreateView, AdminProductCategoryUpdateView, \
    AdminCategoryDeleteView, update_order_status, cancel_order, change_product_is_active_status, \
    change_productcategory_is_active_status, change_user_is_active_status, change_user_is_staff_status

app_name = 'admins'

urlpatterns = [
    path('', AdminIndexView.as_view(), name='index'),
    path('users', AdminUserListView.as_view(), name='admin_users'),
    path('users/create/', AdminUserCreateView.as_view(), name='admin_users_create'),
    path('users/update/<int:pk>', AdminUserUpdateView.as_view(), name='admin_users_update'),
    path('users/update-status/<int:pk>', change_user_is_active_status, name='admin_users_update_status'),
    path('users/update-staff-status/<int:pk>', change_user_is_staff_status, name='admin_users_update_staff_status'),
    path('users/delete/<int:pk>', AdminUserDeleteView.as_view(), name='admin_users_delete'),
    path('users/complete-delete/<int:pk>', AdminUserCompleteDeleteView.as_view(), name='admin_users_complete_delete'),
    path('category', AdminProductCategoryListView.as_view(), name='admin_category'),
    path('category/create/', AdminProductCategoryCreateView.as_view(), name='admin_category_create'),
    path('category/update/<int:pk>', AdminProductCategoryUpdateView.as_view(), name='admin_category_update'),
    path('category/update-status/<int:pk>', change_productcategory_is_active_status,
         name='admin_category_update_status'),
    path('category/delete/<int:pk>', AdminCategoryDeleteView.as_view(), name='admin_category_delete'),
    path('products', AdminProductListView.as_view(), name='admin_products'),
    path('products/category/<int:pk>', AdminProductListView.as_view(), name='admin_products_category'),
    path('products/create/', AdminProductCreateView.as_view(), name='admin_products_create'),
    path('products/update/<int:pk>', AdminProductUpdateView.as_view(), name='admin_products_update'),
    path('products/update-status/<int:pk>', change_product_is_active_status, name='admin_products_update_status'),
    path('products/delete/<int:pk>', AdminProductDeleteView.as_view(), name='admin_products_delete'),
    path('products/complete-delete/<int:pk>', AdminProductCompleteDeleteView.as_view(),
         name='admin_products_complete_delete'),
    path('orders/', AdminOrderListView.as_view(), name='admin_orders'),
    path('orders/delete/<pk>', cancel_order, name='admin_orders_delete'),
    path('update_order_status/<pk>', update_order_status, name='update_order_status'),
]

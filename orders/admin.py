from django.contrib import admin

from orders.models import Order, OrderItem


class OrderItemsAdminInline(admin.TabularInline):
    model = OrderItem
    fields = ('order', 'product', 'quantity')
    extra = 0


@admin.register(Order)
class OrdersAdmin(admin.ModelAdmin):
    fields = ('user', 'status', 'is_active', 'created', 'updated',)
    list_display = ('__str__', 'user', 'status', 'is_active', 'created', 'updated',)
    readonly_fields = ('created', 'updated',)
    inlines = (OrderItemsAdminInline,)
    can_delete = False

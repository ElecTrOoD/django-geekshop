from django.contrib import admin

from products.models import ProductCategory, Product


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    fields = ('name', 'image', 'description', 'price', 'quantity', 'category', 'is_active')
    list_display = ('name', 'price', 'quantity', 'category')
    search_fields = ('name', 'price',)


class ProductAdminInline(admin.TabularInline):
    model = Product
    fields = ('name', 'price', 'quantity')
    extra = 0


@admin.register(ProductCategory)
class ProductCategoryAdmin(admin.ModelAdmin):
    inlines = (ProductAdminInline,)

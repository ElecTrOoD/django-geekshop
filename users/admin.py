from django.contrib import admin

from users.models import User
from baskets.admin import BasketAdmin

# admin.site.register(User)


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('username', 'email', 'is_staff', 'is_active')
    search_fields = ('username', 'email')
    inlines = (BasketAdmin,)

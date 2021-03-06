from django.db import models
from django.utils.functional import cached_property

from products.models import Product
from users.models import User


class Basket(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=0)
    created_timestamp = models.DateTimeField(auto_now_add=True)

    @cached_property
    def get_baskets(self):
        return Basket.objects.filter(user=self.user).select_related()

    def __str__(self):
        return f'Корзина для {self.user.username} | Продукт: {self.product.name}'

    def sum(self):
        return self.quantity * self.product.price

    def total_sum(self):
        return sum(basket.sum() for basket in self.get_baskets)

    def total_quantity(self):
        return sum(basket.quantity for basket in self.get_baskets)

    def get_summary(self):
        baskets = self.get_baskets
        return {
            'total_sum': sum(basket.sum() for basket in baskets),
            'total_quantity': sum(basket.quantity for basket in baskets),
        }

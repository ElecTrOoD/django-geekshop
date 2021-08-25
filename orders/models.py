from django.conf import settings
from django.db import models

from products.models import Product


class Order(models.Model):
    FORMING = 'FM'
    PROCEED = 'PRC'
    DELIVERY = 'DLV'
    DONE = 'DN'
    CANCELED = 'CND'

    STATUSES = (
        (FORMING, 'формирование'),
        (PROCEED, 'в обработке'),
        (DELIVERY, 'доставка'),
        (DONE, 'выдан'),
        (CANCELED, 'отменен'),
    )

    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

    status = models.CharField(max_length=3, choices=STATUSES, default=FORMING)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now_add=True)
    is_active = models.BooleanField(db_index=True, default=True)

    class Meta:
        verbose_name = 'заказ'
        verbose_name_plural = 'заказы'
        ordering = ('-created',)

    def __str__(self):
        return f'Заказ №{self.pk}'

    def get_total_quantity(self):
        items = self.orderitems.select_related()
        return sum(list(map(lambda item: item.quantity, items)))

    def get_total_cost(self):
        items = self.orderitems.select_related()
        return sum(list(map(lambda item: item.get_product_cost, items)))

    def delete(self, using=None, keep_parents=False):
        item_list = self.orderitems.all()
        for item in item_list:
            item.product.quantity += item.quantity
            item.product.save()
        self.is_active = False
        self.status = self.CANCELED
        self.save()


class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name='orderitems')
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=0)

    @property
    def get_product_cost(self):
        return self.quantity * self.product.price

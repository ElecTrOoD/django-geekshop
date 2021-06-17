from django.db import models


class ProductCategory(models.Model):
    name = models.CharField(max_length=255, unique=True)
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField(max_length=255)
    image = models.ImageField(upload_to='products_images', blank=True)
    description = models.CharField(max_length=255, blank=True, null=True)
    price = models.DecimalField(max_digits=8, decimal_places=2)
    quantity = models.PositiveIntegerField(default=0)
    category = models.ForeignKey(ProductCategory, on_delete=models.CASCADE)
    is_active = models.BooleanField(default=False)

    def __str__(self):
        return f'{self.name}'

    def decrement_quantity(self):
        self.quantity -= 1
        if self.quantity == 0:
            self.is_active = False
        self.save()

    def increment_quantity(self):
        if not self.is_active:
            self.is_active = True
        self.quantity += 1
        self.save()

    def set_quantity(self, quantity):
        if not self.is_active:
            self.is_active = True
            self.quantity = quantity
        else:
            self.quantity += quantity
        self.save()

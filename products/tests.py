from django.test import TestCase
from django.test.client import Client

from products.models import ProductCategory, Product


class ProductSmokeTest(TestCase):
    status_code_success = 200

    def SetUp(self):
        category = ProductCategory.objects.create(name='cat1')
        for i in range(10):
            Product.objects.create(
                category=category,
                name=f'prod{i}',
                price=100 + i
            )
        self.client = Client()

    def test_product_urls(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, self.status_code_success)

        response = self.client.get('/products/')
        self.assertEqual(response.status_code, self.status_code_success)

    def test_products_list(self):
        for i in range(1, Product.objects.count() // 3):
            response = self.client.get(f'/products/page/{i}')
            self.assertEqual(response.status_code, self.status_code_success)

    def test_category_list(self):
        for category in ProductCategory.objects.all():
            response = self.client.get(f'/products/?filter={category.name}')
            self.assertEqual(response.status_code, self.status_code_success)

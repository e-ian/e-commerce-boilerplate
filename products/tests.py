from django.test import TestCase
from .models import Category, Product

class ProductModelTests(TestCase):
    def test_create_category(self):
        category = Category.objects.create(name='Electronics')
        self.assertEqual(category.name, 'Electronics')
        self.assertIsNone(category.parent)

    def test_create_product(self):
        category = Category.objects.create(name='Electronics')
        product = Product.objects.create(
            name='Smartphone',
            description='A smart phone with many features',
            price=499.99,
            category=category
        )
        self.assertEqual(product.name, 'Smartphone')
        self.assertEqual(product.description, 'A smart phone with many features')
        self.assertEqual(product.price, 499.99)
        self.assertEqual(product.category, category)

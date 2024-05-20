from django.core.management.base import BaseCommand
from products.models import Category, Product
from users.models import User
from decimal import Decimal
import random


class Command(BaseCommand):
    help = 'Generate sample data for products and categories'

    def handle(self, *args: random.Any, **options: random.Any) -> str | None:
        self.stdout.write('Generating sample data')

        electronics = Category.objects.create(name='Electronics')
        clothing = Category.objects.create(name='Clothing')

        # Create sample products
        Product.objects.bulk_create([
            Product(name='Smartphone', description='A smart phone', price=Decimal('699.99'), category=electronics),
            Product(name='Laptop', description='A powerful laptop', price=Decimal('1299.99'), category=electronics),
            Product(name='T-Shirt', description='A comfortable t-shirt', price=Decimal('19.99'), category=clothing),
            Product(name='Jeans', description='Stylish jeans', price=Decimal('49.99'), category=clothing),
        ])

        self.stdout.write('Sample data generated successfully.')
   

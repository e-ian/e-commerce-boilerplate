from django.test import TestCase
from users.models import User
from products.models import Product, Category
from .models import Order, OrderItem
from decimal import Decimal

class OrderModelTests(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(
            username='testuser',
            email='testuser@example.com',
            password='testpassword',
            shipping_address='123 Test Street'
        )
        self.category = Category.objects.create(name='Electronics')
        self.product1 = Product.objects.create(
            name='Smartphone',
            description='A smart phone with many features',
            price=Decimal('499.99'),
            category=self.category
        )
        self.product2 = Product.objects.create(
            name='Laptop',
            description='A laptop with many features',
            price=Decimal('999.99'),
            category=self.category
        )
    
    def test_create_order(self):
        order = Order.objects.create(
            user=self.user,
            shipping_address=self.user.shipping_address
        )
        OrderItem.objects.create(order=order, product=self.product1, quantity=1)
        OrderItem.objects.create(order=order, product=self.product2, quantity=2)
        order.calculate_total_price()
        self.assertEqual(order.total_price, Decimal('2499.97'))

    def test_order_str(self):
        order = Order.objects.create(
            user=self.user,
            shipping_address=self.user.shipping_address
        )
        self.assertEqual(str(order), f"Order {order.id} by {self.user.username}")

    def test_order_item_str(self):
        order = Order.objects.create(
            user=self.user,
            shipping_address=self.user.shipping_address
        )
        order_item = OrderItem.objects.create(order=order, product=self.product1, quantity=1)
        self.assertEqual(str(order_item), f"1 x {self.product1.name}")

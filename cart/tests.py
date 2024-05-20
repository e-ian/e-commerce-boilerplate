from django.test import TestCase
from users.models import User
from products.models import Product, Category
from .models import Cart, CartItem

class CartModelTests(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(
            username='testuser',
            email='testuser@example.com',
            password='testpassword',
            shipping_address='123 Test Street'
        )
        self.category = Category.objects.create(name='Electronics')
        self.product = Product.objects.create(
            name='Smartphone',
            description='A smart phone with many features',
            price=499.99,
            category=self.category
        )
        self.cart = Cart.objects.create(user=self.user)
    
    def test_create_cart_item(self):
        cart_item = CartItem.objects.create(
            cart=self.cart,
            product=self.product,
            quantity=2
        )
        self.assertEqual(cart_item.cart, self.cart)
        self.assertEqual(cart_item.product, self.product)
        self.assertEqual(cart_item.quantity, 2)

    def test_cart_item_str(self):
        cart_item = CartItem.objects.create(
            cart=self.cart,
            product=self.product,
            quantity=2
        )
        self.assertEqual(str(cart_item), f"2 x {self.product.name}")

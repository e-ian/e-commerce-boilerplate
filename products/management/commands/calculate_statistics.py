# products/management/commands/calculate_statistics.py
from django.core.management.base import BaseCommand
from products.models import Product, Order, OrderItem
from decimal import Decimal

class Command(BaseCommand):
    help = 'Calculate statistics for orders and products'

    def handle(self, *args, **kwargs):
        self.stdout.write('Calculating statistics...')

        # Total number of products
        total_products = Product.objects.count()
        self.stdout.write(f'Total number of products: {total_products}')

        # Total revenue from orders
        total_revenue = Order.objects.aggregate(total_revenue=Sum('total_price'))['total_revenue'] or Decimal('0.00')
        self.stdout.write(f'Total revenue: {total_revenue}')

        # Most sold product
        most_sold_product = OrderItem.objects.values('product').annotate(total_quantity=Sum('quantity')).order_by('-total_quantity').first()
        if most_sold_product:
            product = Product.objects.get(id=most_sold_product['product'])
            self.stdout.write(f'Most sold product: {product.name} (Quantity: {most_sold_product["total_quantity"]})')
        else:
            self.stdout.write('No sales data available.')

        self.stdout.write('Statistics calculated successfully.')


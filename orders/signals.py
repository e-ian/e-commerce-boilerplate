# orders/signals.py
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.core.mail import send_mail
from django.conf import settings
from .models import Order

@receiver(post_save, sender=Order)
def send_order_confirmation_email(sender, instance, created, **kwargs):
    if created:
        subject = f'Order Confirmation - Order #{instance.id}'
        message = f'Thank you for your order, {instance.user.username}!\n\nYour order details:\n\n'
        for item in instance.items.all():
            message += f'{item.quantity} x {item.product.name} - ${item.product.price}\n'
        message += f'\nTotal: ${instance.total_price}\n\nYour order will be shipped to:\n{instance.shipping_address}'
        
        send_mail(
            subject,
            message,
            settings.DEFAULT_FROM_EMAIL,
            [instance.user.email],
            fail_silently=False,
        )

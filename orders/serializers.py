from rest_framework import serializers
from .models import Order


class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = ['id', 'user', 'products', 'total_price', 'created_at']

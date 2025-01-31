from rest_framework import serializers
from core.models import Product, Order

class ProductSerializer(serializers.ModelSerializer):

    class Meta:
        model = Product


class OrderSerializer(serializers.ModelSerializer):

    class Meta:
        model = Order
        fields = ['total_payment', 'paid_in_advance', 'product', 'customer']
        read_only_fields = ('order_id',)
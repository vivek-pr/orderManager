from rest_framework import serializers

from orderProducts.models import Order


class OrderSerializers(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = ['id', 'product', 'quantity', 'amount_paid', 'user', 'created_at']
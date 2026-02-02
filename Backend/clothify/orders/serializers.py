from rest_framework import serializers
from orders.models import Order, OrderItem


class OrderItemSerializer(serializers.ModelSerializer):
    product_name = serializers.CharFiedld(source="product.name", read_only=True)
    product_image = serializers.ImageField(source="product.product_image")

    class Meta:
        model = OrderItem
        fields = [
            "id",
            "product_name",
            "product_image",
            "price_at_purchase",
            "quantity",
        ]

class OrderListSerializer(serializers.ModelSerializer):
    items_count = serializers.IntegerField(source="items.count", read_only=True)

    class Meta:
        model = Order
        fields = [
            "id",
            "total_amount",
            "status",
            "items_count",
            "created_at",
        ]
    
class OrderDetailSerializer(serializers.ModelSerializer):
    items = OrderItemSerializer(many=True, read_only=True)

    class Meta:
        model = Order
        fields = [
            "id",
            "status",
            "total_amount",
            "items",
            "created_at",
        ]
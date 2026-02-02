from carts.models import Cart, CartItem
from rest_framework import serializers


class CartItemSerializer(serializers.ModelSerializer):
    product_name = serializers.CharField(source="product.name", read_only=True)
    product_price = serializers.DecimalField(source="product.price", 
                                             max_digits=10, 
                                             decimal_places=2,
                                             read_only=True)
    class Meta:
       model = CartItem
       fields = [
          "id",
          "product_name",
          "product_price",
          "quantity",
       ]

class CartSerializer(serializers.ModelSerializer):
   items = CartItemSerializer(many=True, read_only=True)
   total_amount = serializers.SerializerMethodField()
   subtotal = serializers.SerializerMethodField()
   class Meta:
      model = Cart
      fields = [
         "id",
         "items",
         "total_amount",
      ] 

      def get_total_amount(self, obj):
        return sum(
           item.product.price * item.quantity
           for item in obj.items.all()
        )
      
      def get_subtotal(self, obj):
         return obj.product.price * obj.quantity
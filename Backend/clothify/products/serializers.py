from products.models import Product, Category
from rest_framework import serializers

class ProductDetailsSerializer(serializers.ModelSerializer):
    category_name = serializers.CharField(source='Category.name',
                                          max_length=30)
    final_price = serializers.SerializerMethodField()
    class Meta:
        model = Product
        fields = [
            "id", 
            "name", 
            "description", 
            "price", 
            "stock", 
            "product_image", 
            "category_name",
            "is_active", 
            "created_at", 
            "updated_at",
            "discount_price",
        ]
        def get_final_price(self, obj):
            return obj.discount_price or obj.price

class ProductListSerializer(serializers.ModelSerializer):
    final_price = serializers.SerializerMethodField()

    class Meta:
        model = Product
        fields = [
            "id",
            "name",
            "final_price",
            "price",
            "discount_price",
            "product_image",
            "stock",
        ]

        def get_final_price(self, obj):
            return obj.discount_price or obj.price

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = [
            "id", 
            "name", 
            "slug", 
            "created_at",
        ]
        read_only_fields = [ 
            "id", "created_at",
        ]

class CategoryDetailSerializer(serializers.ModelSerializer):
    products = ProductSerializer(many=True, read_only=True)

    class Meta:
        model = Category
        fields = [
            "id", 
            "name", 
            "slug", 
            "created_at", 
            "products",
        ]
        read_only_fields = [
            "id", "created",
        ]

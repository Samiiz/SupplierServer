from rest_framework import serializers

from .models import Order, Product, User


class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = "__all__"

    def create(self, validated_data):
        user = User(**validated_data)
        user.set_password(validated_data["password"])
        user.save()
        return user


class UserGetSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ("id", "email", "name", "affiliation", "address", "api")


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = "__all__"

class ProductGetSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ("id", "name", "price")


class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = "__all__"
        extra_kwargs = {'user': {'read_only': True}}


class OrderGetSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = ("id", "user", "product", "created_at")
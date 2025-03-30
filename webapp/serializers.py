from rest_framework import serializers
# from .models import Case, Order, OrderItem
from .models import MTBBike, RoadBike


class MTBBikeSerializer(serializers.ModelSerializer):
    brand = serializers.StringRelatedField()
    frame = serializers.StringRelatedField()
    fork = serializers.StringRelatedField()
    wheelset = serializers.StringRelatedField()
    drivetrain = serializers.StringRelatedField()
    brake = serializers.StringRelatedField()
    handlebar = serializers.StringRelatedField()

    class Meta:
        model = MTBBike
        fields = "__all__"


class RoadBikeSerializer(serializers.ModelSerializer):
    brand = serializers.StringRelatedField()
    frame = serializers.StringRelatedField()
    fork = serializers.StringRelatedField()
    wheelset = serializers.StringRelatedField()
    drivetrain = serializers.StringRelatedField()
    brake = serializers.StringRelatedField()
    handlebar = serializers.StringRelatedField()

    class Meta:
        model = RoadBike
        fields = "__all__"

# class OrderItemSerializer(serializers.ModelSerializer):
#     case = serializers.PrimaryKeyRelatedField(queryset=Case.objects.all())  # Only the ID of the related case
#
#     class Meta:
#         model = OrderItem
#         fields = ['case', 'quantity']
#
#
# class OrderSerializer(serializers.ModelSerializer):
#     items = OrderItemSerializer(many=True)  # Include multiple order items (cases and quantities)
#
#     class Meta:
#         model = Order
#         fields = ['first_name', 'last_name', 'email', 'phone', 'items']
#
#     def create(self, validated_data):
#         # Extract items and create the order
#         items_data = validated_data.pop('items')
#         order = Order.objects.create(**validated_data)
#
#         # Create the OrderItems (cases and quantities)
#         for item_data in items_data:
#             OrderItem.objects.create(order=order, **item_data)
#
#         return order

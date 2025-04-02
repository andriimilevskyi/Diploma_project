from django.contrib.contenttypes.models import ContentType
from rest_framework import serializers
# from .models import Case, Order, OrderItem
from .models import MTBBike, RoadBike, BicycleDetailedImage


class BicycleDetailedImageSerializer(serializers.ModelSerializer):
    image_url = serializers.SerializerMethodField()

    class Meta:
        model = BicycleDetailedImage
        fields = ["id", "image_url"]

    def get_image_url(self, obj):
        if obj.image:
            request = self.context.get("request")
            return request.build_absolute_uri(obj.image.url) if request else obj.image.url
        return None


class MTBBikeSerializer(serializers.ModelSerializer):
    brand = serializers.StringRelatedField()
    frame = serializers.StringRelatedField()
    fork = serializers.StringRelatedField()
    wheelset = serializers.StringRelatedField()
    drivetrain = serializers.StringRelatedField()
    brake = serializers.StringRelatedField()
    handlebar = serializers.StringRelatedField()
    detailed_images = serializers.SerializerMethodField()

    class Meta:
        model = MTBBike
        fields = "__all__"

    def get_detailed_images(self, obj):
        """ Manually fetch all related images """
        images = BicycleDetailedImage.objects.filter(
            content_type=ContentType.objects.get_for_model(obj),
            object_id=obj.id
        )
        return BicycleDetailedImageSerializer(images, many=True, context=self.context).data


class RoadBikeSerializer(serializers.ModelSerializer):
    brand = serializers.StringRelatedField()
    frame = serializers.StringRelatedField()
    fork = serializers.StringRelatedField()
    wheelset = serializers.StringRelatedField()
    drivetrain = serializers.StringRelatedField()
    brake = serializers.StringRelatedField()
    handlebar = serializers.StringRelatedField()
    detailed_images = serializers.SerializerMethodField()

    class Meta:
        model = RoadBike
        fields = "__all__"

    def get_detailed_images(self, obj):
        """ Manually fetch all related images """
        images = BicycleDetailedImage.objects.filter(
            content_type=ContentType.objects.get_for_model(obj),
            object_id=obj.id
        )
        return BicycleDetailedImageSerializer(images, many=True, context=self.context).data

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

from django.contrib.contenttypes.models import ContentType
from rest_framework import serializers
# from .models import Case, Order, OrderItem
from .models import MTBBike, RoadBike, BicycleDetailedImage, Frame, Fork, WheelSet, FrontWheel, RearWheel, Crankset, \
    BottomBracket, Derailleur, Shifter, Cassette, Chain


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


class FrameSerializer(serializers.ModelSerializer):
    # Serialize brand and material as names (not IDs) to improve readability in JSON output
    brand = serializers.CharField(source='brand.name', read_only=True)
    material = serializers.CharField(source='material.material_name', read_only=True)

    class Meta:
        model = Frame
        fields = [
            'id', 'brand', 'series', 'type',
            'wheel_size', 'tyre_size', 'size', 'material',
            'color', 'weight', 'price', 'image'
        ]


class ForkSerializer(serializers.ModelSerializer):
    brand = serializers.CharField(source='brand.name', read_only=True)
    wheel_size = serializers.CharField(source='wheel_size.size', read_only=True)
    axle_type = serializers.CharField(source='axle_type.name', read_only=True)
    brake_mount = serializers.CharField(source='brake_mount.name', read_only=True)

    class Meta:
        model = Fork
        fields = [
            'id', 'brand', 'series', 'type', 'suspension_type',
            'wheel_size', 'travel', 'offset', 'stem_diameter',
            'axle_type', 'brake_mount', 'remote', 'tyre_size',
            'rotor_size_max', 'price', 'weight', 'image'
        ]


class CranksetSerializer(serializers.ModelSerializer):
    brand = serializers.CharField(source='brand.name', read_only=True)

    class Meta:
        model = Crankset
        fields = [
            'id', 'brand', 'series', 'gradation', 'gearing',
            'crank_arm_length', 'chainline', 'price', 'weight', 'image'
        ]


class BottomBracketSerializer(serializers.ModelSerializer):
    brand = serializers.CharField(source='brand.name', read_only=True)

    class Meta:
        model = BottomBracket
        fields = ['id', 'brand', 'series', 'type', 'shell_width', 'axle_diameter', 'price', 'weight', 'image']


class DerailleurSerializer(serializers.ModelSerializer):
    brand = serializers.CharField(source='brand.name', read_only=True)

    class Meta:
        model = Derailleur
        fields = [
            'id', 'brand', 'series', 'gearing', 'type',
            'smallest_gear', 'biggest_gear', 'price', 'weight', 'image'
        ]


class ShifterSerializer(serializers.ModelSerializer):
    brand = serializers.CharField(source='brand.name', read_only=True)
    mount = serializers.CharField(source='mount.mount_standard', read_only=True)

    class Meta:
        model = Shifter
        fields = [
            'id', 'brand', 'series', 'gearing', 'type',
            'mount', 'price', 'weight', 'image'
        ]


class CassetteSerializer(serializers.ModelSerializer):
    brand = serializers.CharField(source='brand.name', read_only=True)
    freehub_standard = serializers.CharField(source='freehub_standard.freehub_name', read_only=True)

    class Meta:
        model = Cassette
        fields = [
            'id', 'brand', 'series', 'gearing', 'gradation',
            'gradation_all', 'smallest_gear', 'biggest_gear',
            'freehub_standard', 'weight', 'price', 'image'
        ]


class ChainSerializer(serializers.ModelSerializer):
    brand = serializers.CharField(source='brand.name', read_only=True)

    class Meta:
        model = Chain
        fields = [
            'id', 'brand', 'series',
            'links_num', 'gearing', 'clousing_type',
            'directional', 'price', 'weight', 'image',
        ]


class FrontWheelSerializer(serializers.ModelSerializer):
    image = serializers.ImageField(read_only=True)
    brand = serializers.CharField(source='brand.name', read_only=True)

    class Meta:
        model = FrontWheel
        fields = ['id', 'brand', 'image']


class RearWheelSerializer(serializers.ModelSerializer):
    image = serializers.ImageField(read_only=True)
    brand = serializers.CharField(source='brand.name', read_only=True)

    class Meta:
        model = RearWheel
        fields = ['id', 'brand', 'image']


class WheelSetSerializer(serializers.ModelSerializer):
    brand = serializers.CharField(source='brand.name', read_only=True)
    wheel_size = serializers.CharField(source='wheel_size.size', read_only=True)
    rotor_mount = serializers.CharField(source='rotor_mount.rotor_mount', read_only=True)
    front_wheel = FrontWheelSerializer(read_only=True)
    rear_wheel = RearWheelSerializer(read_only=True)

    class Meta:
        model = WheelSet
        fields = [
            'id', 'brand', 'series', 'wheel_size', 'spokes_num', 'rotor_mount',
            'tubeless_ready', 'front_wheel', 'rear_wheel', 'price', 'weight', 'wheelset_image'
        ]
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

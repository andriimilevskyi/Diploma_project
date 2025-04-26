from django.contrib import admin
from django.utils.html import mark_safe
from django.contrib.contenttypes.admin import GenericTabularInline
# from .models import Case, Order, OrderItem
from .models import Frame, Fork, Derailleur, FrontDerailleur, Cassette, Chain, Crankset, BottomBracket, Shifter, \
    BrakeLever, BrakeCaliper, BrakeRotor, WheelSet, BrakePads, Brand, Application, WheelSize, TyreSize, AxleType, \
    BBStandard, FrontDerailleurMount, BrakeMountStandard, Material, RotorMountType, RotorDiameter, TubeDiameter, \
    HandlebarFlat, HandlebarDrop, HandlebarMount, Stem, ChainringMountStandard, FreehubStandard, BrakePadsCompound, \
    BrakeHoseConnection, BrakeActuation, Brakes, DiskBrakeAdapter, Rim, FrontHub, RearHub, WheelLacing, FrontWheel, \
    RearWheel, RearShock, RearShockMount, Drivetrain, RoadBike, MTBBike, BicycleDetailedImage, \
    MTBBicycleConfiguration


class HiddenModelAdmin(admin.ModelAdmin):
    def get_model_perms(self, request):
        # hides models from home
        return {}


# Register your models here.
# class CaseAdmin(admin.ModelAdmin):
#     list_display = ('id', 'name', 'color', 'material', 'price', 'created_at')
#     search_fields = ('name', 'color', 'material')
#     list_filter = ('color', 'material')
#     ordering = ('created_at',)

# admin.site.register(Case)
# admin.site.register(Order)
# admin.site.register(OrderItem)
# , iPhoneCaseAdmin)
@admin.register(Brand)
class BrandAdmin(HiddenModelAdmin):
    list_display = ("name",)


@admin.register(Application)
class ApplicationAdmin(HiddenModelAdmin):
    list_display = ("name",)


class BicycleDetailedImageInline(GenericTabularInline):
    model = BicycleDetailedImage
    extra = 1  # Количество пустых полей для добавления новых изображений

    readonly_fields = ["preview"]

    def preview(self, obj):
        if obj.image:
            return mark_safe(
                f'<img src="{obj.image.url}" width="48%" height="30%" style="object-fit: cover; border-radius: 5px;"/>')
        return "No Image"

    preview.short_description = "Image Preview"


@admin.register(WheelSize)
class WheelSizeAdmin(HiddenModelAdmin):
    list_display = ("size",)


@admin.register(TyreSize)
class TyreSizeAdmin(HiddenModelAdmin):
    list_display = ("size",)


@admin.register(AxleType)
class AxleTypeAdmin(HiddenModelAdmin):
    list_display = ("type", "diameter", "length", "side")


@admin.register(BBStandard)
class BBStandardAdmin(HiddenModelAdmin):
    list_display = ("name", "type")


@admin.register(FrontDerailleurMount)
class FrontDerailleurMountAdmin(HiddenModelAdmin):
    list_display = ("name", "type")


@admin.register(RotorMountType)
class RotorMountTypeAdmin(HiddenModelAdmin):
    list_display = ("mount_type",)


@admin.register(RotorDiameter)
class RotorDiameterAdmin(HiddenModelAdmin):
    list_display = ("diameter",)


@admin.register(BrakeMountStandard)
class BrakeMountStandardAdmin(HiddenModelAdmin):
    list_display = ("name", "rotor_size")


@admin.register(TubeDiameter)
class TubeDiameterAdmin(HiddenModelAdmin):
    list_display = ("diameter",)


@admin.register(Material)
class MaterialAdmin(HiddenModelAdmin):
    list_display = ("material_name",)


@admin.register(Frame)
class FrameAdmin(admin.ModelAdmin):
    list_display = ("brand", "series", "size", "image")


@admin.register(Fork)
class ForkAdmin(admin.ModelAdmin):
    list_display = ("brand", "series", "image")


@admin.register(RearShockMount)
class RearShockMountAdmin(HiddenModelAdmin):
    list_display = ("mount_type",)


@admin.register(RearShock)
class RearShockAdmin(admin.ModelAdmin):
    list_display = ("brand", "series", "mount", "size", "stroke")


@admin.register(Derailleur)
class DerailleurAdmin(admin.ModelAdmin):
    list_display = ("brand", "series", "image")


@admin.register(FrontDerailleur)
class FrontDerailleurAdmin(admin.ModelAdmin):
    list_display = ("brand", "series", "image")


@admin.register(Cassette)
class CassetteAdmin(admin.ModelAdmin):
    list_display = ("brand", "series", "image")


@admin.register(Chain)
class ChainAdmin(admin.ModelAdmin):
    list_display = ("brand", "series", "image")


@admin.register(Crankset)
class CranksetAdmin(admin.ModelAdmin):
    list_display = ("brand", "series", "image")


@admin.register(BottomBracket)
class BottomBracketAdmin(admin.ModelAdmin):
    list_display = ("brand", "series", "image")


@admin.register(Shifter)
class ShifterAdmin(admin.ModelAdmin):
    list_display = ("brand", "series", "image")


@admin.register(BrakeLever)
class BrakeLeverAdmin(admin.ModelAdmin):
    list_display = ("brand", "series", "image")


@admin.register(BrakeCaliper)
class BrakeCaliperAdmin(admin.ModelAdmin):
    list_display = ("brand", "series", "image")


@admin.register(BrakeRotor)
class BrakeRotorAdmin(admin.ModelAdmin):
    list_display = ("brand", "series", "image")


@admin.register(BrakePads)
class BrakePadsAdmin(admin.ModelAdmin):
    list_display = ("brand", "series", "image")


@admin.register(HandlebarFlat)
class HandlebarMTBAdmin(admin.ModelAdmin):
    list_display = ("brand", "series", "image")


@admin.register(HandlebarDrop)
class HandlebarRoadAdmin(admin.ModelAdmin):
    list_display = ("brand", "series", "image")


@admin.register(HandlebarMount)
class HandlebarMountAdmin(admin.ModelAdmin):
    list_display = ("mount_standard",)


@admin.register(Stem)
class StemAdmin(admin.ModelAdmin):
    list_display = ("brand", "series", "image")


@admin.register(ChainringMountStandard)
class ChainringMountStandardAdmin(HiddenModelAdmin):
    list_display = ("type",)


@admin.register(FreehubStandard)
class FreehubStandardAdmin(HiddenModelAdmin):
    list_display = ("freehub_name",)


@admin.register(BrakePadsCompound)
class BrakePadsCompoundAdmin(HiddenModelAdmin):
    list_display = ("compound_type",)


@admin.register(BrakeHoseConnection)
class BrakeHoseConnectionAdmin(HiddenModelAdmin):
    list_display = ("connection_type",)


@admin.register(BrakeActuation)
class BrakeActuationAdmin(HiddenModelAdmin):
    list_display = ("actuation_type",)


@admin.register(Brakes)
class BrakesAdmin(admin.ModelAdmin):
    list_display = ("brand", "series", "actuation")


@admin.register(DiskBrakeAdapter)
class DiskBrakeAdapterAdmin(admin.ModelAdmin):
    list_display = ("brand", "series", "mount", "caliper_mount")


@admin.register(Rim)
class RimAdmin(admin.ModelAdmin):
    list_display = ("brand", "series", "wheel_size", "spokes_num", "material")


@admin.register(FrontHub)
class FrontHubAdmin(admin.ModelAdmin):
    list_display = ("brand", "series", "spoke_holes", "rotor_mount", "axle_type")


@admin.register(RearHub)
class RearHubAdmin(admin.ModelAdmin):
    list_display = ("brand", "series", "image", "spoke_holes", "rotor_mount", "axle_type", "freehub")


@admin.register(WheelLacing)
class WheelLacingAdmin(HiddenModelAdmin):
    list_display = ("lacing_type",)


@admin.register(FrontWheel)
class FrontWheelAdmin(admin.ModelAdmin):
    list_display = ("brand", "series", "application", "wheel_size", "tubeless_ready", "spokes_num")


@admin.register(RearWheel)
class RearWheelAdmin(admin.ModelAdmin):
    list_display = ("brand", "series", "application", "wheel_size", "tubeless_ready", "spokes_num")


@admin.register(WheelSet)
class WheelSetAdmin(admin.ModelAdmin):
    list_display = ("brand", "series",)


@admin.register(Drivetrain)
class DrivetrainAdmin(admin.ModelAdmin):
    list_display = ("brand", "series",)


@admin.register(RoadBike)
class RoadBikeAdmin(admin.ModelAdmin):
    list_display = ("brand", "series", "preview_image")
    inlines = [BicycleDetailedImageInline]


readonly_fields = ["preview_image_admin"]


def preview_image_admin(self, obj):
    if obj.preview_image:
        return mark_safe(
            f'<img src="{obj.preview_image.url}" width="500" height="300" style="object-fit: cover; border-radius: 5px;"/>')
    return "No Image"


preview_image_admin.short_description = "Preview Image"


@admin.register(MTBBike)
class MTBBikeAdmin(admin.ModelAdmin):
    list_display = ("brand", "series", "frame", "fork", "wheelset", "drivetrain", "brake", "handlebar", "preview_image")
    list_select_related = ("brand", "frame", "fork", "wheelset", "drivetrain", "brake", "handlebar")
    inlines = [BicycleDetailedImageInline]

    readonly_fields = ["preview_image_admin"]

    def preview_image_admin(self, obj):
        if obj.preview_image:
            return mark_safe(
                f'<img src="{obj.preview_image.url}" width="500" height="300" style="object-fit: cover; border-radius: 5px;"/>')
        return "No Image"

    preview_image_admin.short_description = "Preview Image"


@admin.register(MTBBicycleConfiguration)
class MTBBicycleConfigurationAdmin(admin.ModelAdmin):
    list_display = ("id", "name",)

# @admin.register(Case)
# class CaseAdmin(admin.ModelAdmin):
#     list_display = ('name', 'type', 'color', 'material', 'price', 'created_at', 'image')
#     list_filter = ('type', 'color', 'material', 'price')
#     search_fields = ('name', 'type', 'color', 'material')
#     ordering = ('type', 'name')
#     readonly_fields = ('created_at', 'updated_at')
#
#     def image_preview(self, obj):
#         if obj.image:
#             return f"<img src='{obj.image.url}' width='50' height='50' />"
#         return "No Image"
#
#     image_preview.allow_tags = True
#     image_preview.short_description = "Image Preview"
#
#     fieldsets = (
#         ("Basic Information", {
#             "fields": ('name', 'type', 'color', 'material', 'price', 'image')
#         }),
#         ("Details", {
#             "fields": ('s_description', 'description', 'features'),
#         }),
#         ("Timestamps", {
#             "fields": ('created_at', 'updated_at'),
#         }),
#     )
#
#
# class OrderItemInline(admin.TabularInline):
#     model = OrderItem
#     extra = 1
#     readonly_fields = ('total_price',)
#     fields = ('case', 'quantity', 'total_price')
#
#     def total_price(self, obj):
#         return obj.total_price
#
#     total_price.short_description = 'Total Price (Item)'
#
#
# @admin.register(Order)
# class OrderAdmin(admin.ModelAdmin):
#     list_display = ('id', 'first_name', 'last_name', 'email', 'phone', 'datetime', 'total_price')
#     list_filter = ('datetime',)
#     search_fields = ('first_name', 'last_name', 'email', 'phone')
#     date_hierarchy = 'datetime'
#     readonly_fields = ('datetime', 'total_price')
#     inlines = [OrderItemInline]
#
#     def total_price(self, obj):
#         return obj.total_price
#
#     total_price.short_description = 'Total Price (Order)'
#
#
# @admin.register(OrderItem)
# class OrderItemAdmin(admin.ModelAdmin):
#     list_display = ('order', 'case', 'quantity', 'total_price')
#     list_filter = ('case__type',)
#     search_fields = ('order__id', 'case__name')
#     readonly_fields = ('total_price',)
#
#     def total_price(self, obj):
#         return obj.total_price

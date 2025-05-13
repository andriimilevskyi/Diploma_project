from django.db import models
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType
from django.contrib.auth.models import AbstractUser


# https://acode.com.ua/inheritance-python/

# Create your models here.


class User(AbstractUser):
    email = models.EmailField(unique=True)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    delivery_address = models.TextField()
    phone_number = models.CharField(max_length=15, blank=True, null=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

    # def get_order_history(self):
    #     return self.orders.all()

    # def get_saved_configurations(self):
    #     return self.bicycle_configurations.all()


# class Case(models.Model):
#     name = models.CharField(max_length=100, verbose_name="Case Name")
#     type = models.CharField(max_length=50, choices=[
#         ('A14', 'iPhone 14'),
#         ('A14 Plus', 'iPhone 14 Plus'),
#         ('A14 Pro', 'iPhone 14 Pro'),
#         ('A14 Pro Max', 'iPhone 14 Pro Max'),
#         ('ASE2', 'iPhone SE 2'),
#         ('ASE3', 'iPhone SE 3'),
#         ('A15', 'iPhone 15'),
#         ('A15 Plus', 'iPhone 15 Plus'),
#         ('A15 Pro', 'iPhone 15 Pro'),
#         ('A15 Pro Max', 'iPhone 15 Pro Max'),
#         ('A16', 'iPhone 16'),
#         ('A16 Plus', 'iPhone 16 Plus'),
#         ('A16 Pro', 'iPhone 16 Pro Max'),
#         ('A16 Pro Max', 'iPhone 16 Pro Max'),
#     ], verbose_name="Type")
#     color = models.CharField(max_length=50, verbose_name="Color")
#     material = models.CharField(max_length=50, verbose_name="Material")
#     features = models.TextField(verbose_name="Features")
#     price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Price")
#     s_description = models.CharField(max_length=150, verbose_name="Short Description")
#     description = models.TextField(verbose_name="Full Description")
#     image = models.ImageField(upload_to='case_images/', blank=True, null=True, verbose_name="Image")
#     created_at = models.DateTimeField(auto_now_add=True)
#     updated_at = models.DateTimeField(auto_now=True)
#
#     def __str__(self):
#         return f"{self.name} ({self.type})"


class Brand(models.Model):
    name = models.CharField(max_length=100, verbose_name="Brand Name", unique=True, db_index=True)

    def __str__(self):
        return self.name


class Application(models.Model):
    name = models.CharField(max_length=100, verbose_name="Application name", unique=True, db_index=True)

    def __str__(self):
        return self.name


class Material(models.Model):
    material_name = models.CharField(max_length=50, verbose_name="Material", unique=True, db_index=True)

    def __str__(self):
        return self.material_name


class WheelSize(models.Model):
    size = models.CharField(max_length=15, verbose_name="Wheel Size", unique=True, db_index=True)

    def __str__(self):
        return self.size


class TyreSize(models.Model):
    size = models.CharField(max_length=15, verbose_name="Tyre Size", unique=True, db_index=True)

    def __str__(self):
        return self.size


class AxleType(models.Model):
    type = models.CharField(max_length=50, verbose_name="Axle type")
    diameter = models.PositiveIntegerField(verbose_name="Axle diameter")
    length = models.PositiveIntegerField(verbose_name="Axle length")
    side = models.CharField(max_length=15, verbose_name="Axle side")

    def __str__(self):
        return f"{self.side}/{self.type}, {self.diameter}mm/{self.length}mm"


class BBStandard(models.Model):
    name = models.CharField(max_length=15, verbose_name="Bottom Bracket standard name", db_index=True)
    type = models.CharField(max_length=15, verbose_name="Bottom Bracket standard type", db_index=True)

    def __str__(self):
        return f"{self.type}/{self.name}"


class FrontDerailleurMount(models.Model):
    name = models.CharField(max_length=15, verbose_name="Front Derailleur Mount standard name", db_index=True)
    type = models.CharField(max_length=15, verbose_name="Front Derailleur Mount standard type", null=True, blank=True)

    def __str__(self):
        return f"{self.name}, {self.type or 'N/A'}"


class RotorDiameter(models.Model):
    diameter = models.PositiveIntegerField(verbose_name="Rotor diameter", unique=True, db_index=True)

    def __str__(self):
        return f"{self.diameter}mm"


class RotorMountType(models.Model):
    mount_type = models.CharField(max_length=50, verbose_name="Rotor Mount Type", unique=True, db_index=True)

    def __str__(self):
        return self.mount_type


class BrakeMountStandard(models.Model):
    name = models.CharField(max_length=50, verbose_name="Brake Mount standard name", unique=True, db_index=True)
    rotor_size = models.ForeignKey(RotorDiameter, verbose_name="Rotor size in mm", on_delete=models.PROTECT,
                                   null=True, blank=True)

    def __str__(self):
        return f"{self.name} ({self.rotor_size})" if self.rotor_size else self.name


class TubeDiameter(models.Model):
    diameter = models.DecimalField(max_digits=3, decimal_places=1, verbose_name="Diameter of tube for Stem",
                                   unique=True, db_index=True)

    def __str__(self):
        return f"{self.diameter}mm"


class RearShockMount(models.Model):
    mount_type = models.CharField(max_length=100, verbose_name="Rear Shock mount type")

    def __str__(self):
        return f"{self.mount_type}"


# Базовий клас для загальних характеристик велосипедних компонентів
class BikeComponent(models.Model):
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE, verbose_name="Brand name", db_index=True)
    series = models.CharField(max_length=100, verbose_name="Series Name", db_index=True)
    application = models.ForeignKey(Application, on_delete=models.CASCADE, verbose_name="Application", db_index=True)
    material = models.ForeignKey(Material, on_delete=models.PROTECT, verbose_name="Material", db_index=True)
    features = models.TextField(verbose_name="Features", blank=True, null=True)
    technology = models.TextField(verbose_name="Technology", blank=True, null=True)
    color = models.CharField(max_length=50, verbose_name="Color", db_index=True)
    weight = models.DecimalField(max_digits=5, decimal_places=3, verbose_name="Weight (kg)", null=True, blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Price (€)", null=True, blank=True)
    manufacturer_num = models.CharField(max_length=15, verbose_name="Manufacturer number", db_index=True)

    class Meta:
        abstract = True


class Frame(BikeComponent):
    type = models.CharField(max_length=100, verbose_name="Type")
    wheel_size = models.ForeignKey(WheelSize, on_delete=models.PROTECT, db_index=True)
    tyre_size = models.ForeignKey(TyreSize, on_delete=models.PROTECT, verbose_name="Max Tyre size")
    axle_type = models.ForeignKey(AxleType, on_delete=models.PROTECT, verbose_name="Axle type")
    size = models.CharField(max_length=50, verbose_name="Size", db_index=True)
    seatpost = models.PositiveIntegerField(verbose_name="Seatpost")
    min_rider_height = models.DecimalField(max_digits=4, decimal_places=1, verbose_name="Min Rider Height (cm)",
                                           null=True, blank=True)
    max_rider_height = models.DecimalField(max_digits=4, decimal_places=1, verbose_name="Max Rider Height (cm)",
                                           null=True, blank=True)
    bb_standard = models.ForeignKey(BBStandard, on_delete=models.PROTECT, verbose_name="Bottom Bracket Standard")
    fork_travel = models.PositiveIntegerField(verbose_name="Fork Travel", blank=True, null=True)

    full_suspension = models.BooleanField(verbose_name="Full Suspension Bike")
    rs_size_length = models.PositiveIntegerField(verbose_name="Size Eye-to-Eye in mm", null=True, blank=True)
    rs_stroke = models.DecimalField(max_digits=4, decimal_places=1, verbose_name="Stroke in mm", null=True, blank=True)
    rs_mount = models.ForeignKey(RearShockMount, on_delete=models.PROTECT, verbose_name="Rear Shock Mount", null=True,
                                 blank=True)
    front_derailleur_mount = models.ForeignKey(FrontDerailleurMount, on_delete=models.PROTECT,
                                               verbose_name="Front Derailleur Mount", null=True, blank=True)
    brake_mount = models.ForeignKey(BrakeMountStandard, on_delete=models.PROTECT, verbose_name="Brake Mount")
    chainring_size_max = models.CharField(max_length=50, verbose_name="Max Chainring Size")
    image = models.ImageField(upload_to='components/frames/', verbose_name="Frame Image", null=True, blank=True)

    def clean(self):
        from django.core.exceptions import ValidationError

        if not self.full_suspension:
            if self.rs_size_length or self.rs_stroke or self.rs_mount:
                raise ValidationError("Rear shock fields should be empty if the frame is not full suspension.")

    def __str__(self):
        return f"{self.brand.name} {self.series} ({self.size}, {self.seatpost}mm) - {self.type}"


class Fork(BikeComponent):
    type = models.CharField(max_length=100, verbose_name="Type")
    wheel_size = models.ForeignKey(WheelSize, on_delete=models.CASCADE)
    suspension_type = models.CharField(max_length=100, verbose_name="Suspension type")
    stem_diameter = models.ForeignKey(TubeDiameter, on_delete=models.PROTECT, verbose_name="Steerer Tube Diameter")
    travel = models.PositiveIntegerField(verbose_name="Fork Travel in mm")
    offset = models.PositiveIntegerField(verbose_name="Offset in mm")
    axle_type = models.ForeignKey(AxleType, on_delete=models.CASCADE, verbose_name="Axle type")
    brake_mount = models.ForeignKey(BrakeMountStandard, on_delete=models.PROTECT, verbose_name="Brake Mount")
    remote = models.BooleanField(verbose_name="Remote control")
    tyre_size = models.ForeignKey(TyreSize, on_delete=models.CASCADE, verbose_name="Max Tyre size")
    rotor_size_max = models.ForeignKey(RotorDiameter, on_delete=models.PROTECT, verbose_name="Max Rotor size")
    image = models.ImageField(upload_to='components/forks/', verbose_name="Fork Image", null=True, blank=True)

    def __str__(self):
        return f"{self.brand.name} {self.series} {self.wheel_size} {self.travel}mm/{self.suspension_type}"


class RearShock(BikeComponent):
    suspension_type = models.CharField(max_length=100, verbose_name="Suspension Type")
    size = models.PositiveIntegerField(verbose_name="Size in mm")
    stroke = models.DecimalField(max_digits=4, decimal_places=1, verbose_name="Stroke in mm")
    mount = models.ForeignKey(RearShockMount, on_delete=models.PROTECT, verbose_name="Rear Shock Mount")

    def __str__(self):
        return f"{self.brand.name} {self.series} ({self.size}x{self.stroke}, {self.mount})"


class Handlebar(BikeComponent):
    """Базова модель для керма (MTB/Road)."""
    width = models.IntegerField(verbose_name="Handlebar width (mm)")
    stem_clamp = models.ForeignKey("TubeDiameter", on_delete=models.PROTECT, verbose_name="Stem clamp size")

    class Meta:
        abstract = True


class HandlebarFlat(Handlebar):
    rise = models.IntegerField(verbose_name="Handlebar rise")
    backsweep = models.IntegerField(verbose_name="Handlebar backsweep (°)")
    upsweep = models.IntegerField(verbose_name="Handlebar upsweep (°)")
    image = models.ImageField(upload_to="components/handlebars/mtb/", verbose_name="MTB Handlebar Image", null=True,
                              blank=True)

    def __str__(self):
        return f"{self.brand} {self.series} {self.width}mm ({self.stem_clamp}mm)"


class HandlebarDrop(Handlebar):
    drop = models.IntegerField(verbose_name="Handlebar drop")
    reach = models.IntegerField(verbose_name="Handlebar reach")
    flare = models.IntegerField(verbose_name="Handlebar flare (°)")
    internal_cable_routing = models.BooleanField(verbose_name="Internal cable routing")
    image = models.ImageField(upload_to="components/handlebars/road/", verbose_name="Road Handlebar Image", null=True,
                              blank=True)

    def __str__(self):
        return f"{self.brand} {self.series} {self.width}mm ({self.stem_clamp}mm)"


class Stem(BikeComponent):
    steerer_clamp = models.ForeignKey("TubeDiameter", related_name="steerer_clamp_stems", on_delete=models.PROTECT,
                                      verbose_name="Steerer Tube Diameter")
    handlebar_clamp = models.ForeignKey("TubeDiameter", related_name="handlebar_clamp_stems", on_delete=models.PROTECT,
                                        verbose_name="Handlebar clamp size")
    length = models.IntegerField(verbose_name="Stem length (mm)")
    angle = models.IntegerField(verbose_name="Stem angle (°)")
    stack_height = models.IntegerField(verbose_name="Stack height")
    image = models.ImageField(upload_to="components/stems/", verbose_name="Stem Image", null=True, blank=True)

    def __str__(self):
        return f"{self.brand} {self.series} {self.material} ({self.length}mm/{self.angle}°)"


class ChainringMountStandard(models.Model):
    type = models.CharField(max_length=100, verbose_name="Chainring mount standard type")

    def __str__(self):
        return self.type


class Crankset(BikeComponent):
    chainring_mount = models.ForeignKey("ChainringMountStandard", on_delete=models.PROTECT,
                                        verbose_name="Chainring Mount Standard")
    gradation = models.CharField(max_length=15, verbose_name="Chainrings gradation (smallest-biggest)T")
    gearing = models.IntegerField(verbose_name="Gears count (x-speed)")
    crank_arm_length = models.DecimalField(max_digits=5, decimal_places=1, verbose_name="Crank Arm length")
    axle_diameter = models.IntegerField(verbose_name="Axle diameter in mm")
    chainline = models.DecimalField(max_digits=3, decimal_places=1, verbose_name="Chainline in mm", null=True)
    bb_standard = models.ForeignKey("BBStandard", on_delete=models.PROTECT, verbose_name="Bottom Bracket standard")
    image = models.ImageField(upload_to='components/cranksets/', verbose_name="Crankset Image", null=True, blank=True)

    def __str__(self):
        return f"{self.brand} {self.series} {self.gearing} {self.gradation} {self.chainring_mount}"


class BottomBracket(BikeComponent):
    type = models.CharField(max_length=100, verbose_name="Type")
    shell_width = models.IntegerField(verbose_name="Shell width in mm")
    axle_diameter = models.IntegerField(verbose_name="Axle diameter in mm")
    image = models.ImageField(upload_to='components/bottom_brackets/', verbose_name="Bottom Bracket Image", null=True,
                              blank=True)

    def __str__(self):
        return f"{self.brand} {self.series} {self.type}"


class FreehubStandard(models.Model):
    freehub_name = models.CharField(max_length=50, verbose_name="Freehub standard")

    def __str__(self):
        return self.freehub_name


class Cassette(BikeComponent):
    gearing = models.IntegerField(verbose_name="Gears count (x-speed)")
    gradation = models.CharField(max_length=10, verbose_name="Gradation (smallest-biggest)")
    gradation_all = models.CharField(max_length=100, verbose_name="All gradation", null=True)
    smallest_gear = models.IntegerField(verbose_name="Smallest star")
    biggest_gear = models.IntegerField(verbose_name="Biggest star")
    freehub_standard = models.ForeignKey(FreehubStandard, on_delete=models.PROTECT, verbose_name="Freehub standard")
    image = models.ImageField(upload_to='components/cassettes/', verbose_name="Cassette Image", null=True, blank=True)

    def __str__(self):
        return f"{self.brand} {self.series} {self.gearing} ({self.gradation}, {self.freehub_standard})"


class Chain(BikeComponent):
    links_num = models.IntegerField(verbose_name="Number of links")
    gearing = models.IntegerField(verbose_name="Gears count (x-speed)")
    clousing_type = models.CharField(max_length=15, verbose_name="Chain closing type")
    directional = models.BooleanField(verbose_name="Directional chain")
    image = models.ImageField(upload_to='components/chains/', verbose_name="Chain Image", null=True, blank=True)

    def __str__(self):
        return f"{self.brand} {self.series} {self.gearing}"


class Derailleur(BikeComponent):
    gearing = models.IntegerField(verbose_name="Gears count (x-speed)")
    type = models.CharField(max_length=100, verbose_name="Type")
    smallest_gear = models.IntegerField(verbose_name="Smallest star compatible")
    biggest_gear = models.IntegerField(verbose_name="Biggest star compatible")
    image = models.ImageField(upload_to='components/derailleurs/', verbose_name="Derailleur Image", null=True,
                              blank=True)

    def __str__(self):
        return f"{self.brand} {self.series} {self.gearing}"


class FrontDerailleur(BikeComponent):
    gearing = models.IntegerField(verbose_name="Gears count (x-speed)")
    type = models.CharField(max_length=100, verbose_name="Type")
    chainline = models.DecimalField(max_digits=2, decimal_places=1, verbose_name="Chainline in mm")
    chainring_size_max = models.CharField(max_length=50, verbose_name="Max Chainring Size")
    capacity = models.IntegerField(verbose_name="Capacity (x-tooth)")
    mount = models.ForeignKey("FrontDerailleurMount", on_delete=models.PROTECT, verbose_name="Front Derailleur Mount")
    image = models.ImageField(upload_to='components/front_derailleurs/', verbose_name="Front Derailleur Image",
                              null=True, blank=True)

    def __str__(self):
        return f"{self.brand} {self.series} {self.gearing}"


class HandlebarMount(models.Model):
    mount_standard = models.CharField(max_length=50, verbose_name="Handlebar mount type")

    # Shifters etc.

    def __str__(self):
        return self.mount_standard


class Shifter(BikeComponent):
    gearing = models.IntegerField(verbose_name="Gears count (x-speed)")
    type = models.CharField(max_length=100, verbose_name="Type")
    mount = models.ForeignKey(HandlebarMount, on_delete=models.PROTECT, verbose_name="Mount type")
    image = models.ImageField(upload_to='components/shifters/', verbose_name="Shifter Image", null=True, blank=True)

    def __str__(self):
        return f"{self.brand} {self.series} {self.gearing}"


class Drivetrain(models.Model):
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE, verbose_name="Brand name")
    series = models.CharField(max_length=100, verbose_name="Series Name")
    crankset = models.ForeignKey(Crankset, on_delete=models.PROTECT, verbose_name="Crankset")
    bottom_bracket = models.ForeignKey(BottomBracket, on_delete=models.PROTECT, verbose_name="Bottom Bracket")
    cassette = models.ForeignKey(Cassette, on_delete=models.PROTECT, verbose_name="Cassette")
    chain = models.ForeignKey(Chain, on_delete=models.PROTECT, verbose_name="Chain")
    derailleur = models.ForeignKey(Derailleur, on_delete=models.PROTECT, verbose_name="Rear Derailleur")
    front_derailleur = models.ForeignKey(FrontDerailleur, on_delete=models.PROTECT, verbose_name="Front Derailleur",
                                         null=True, blank=True)
    shifter = models.ForeignKey(Shifter, on_delete=models.PROTECT, verbose_name="Shifter")

    def __str__(self):
        return f"{self.brand} {self.series} Drivetrain"


class BrakePadsCompound(models.Model):
    compound_type = models.CharField(max_length=15, verbose_name="Pads compound material")

    def __str__(self):
        return self.compound_type


class BrakeHoseConnection(models.Model):
    connection_type = models.CharField(max_length=15, verbose_name="Brake hose connection type")

    def __str__(self):
        return self.connection_type


class BrakePads(BikeComponent):
    compound = models.ForeignKey(BrakePadsCompound, on_delete=models.PROTECT, verbose_name="Compound type")
    plate_material = models.ForeignKey(Material, on_delete=models.PROTECT, verbose_name="Plate material",
                                       related_name='brakepads_plate_material')
    cooling_fins = models.BooleanField(verbose_name="Cooling fins")
    image = models.ImageField(upload_to='components/brake_pads/', verbose_name="Brake pads Image", null=True,
                              blank=True)

    def __str__(self):
        return f"{self.brand} {self.series} {self.compound}"


class BrakeActuation(models.Model):
    actuation_type = models.CharField(max_length=15, verbose_name="Brake actuation type")

    def __str__(self):
        return self.actuation_type


class BrakeRotor(BikeComponent):
    mount = models.ForeignKey(RotorMountType, on_delete=models.PROTECT, verbose_name="Mount type")
    diameter = models.ForeignKey(RotorDiameter, on_delete=models.PROTECT, verbose_name="Rotor diameter")
    pads_compatibility = models.ForeignKey(BrakePadsCompound, on_delete=models.PROTECT,
                                           verbose_name="Brake pads compound compatibility",
                                           null=True, blank=True)
    image = models.ImageField(upload_to='components/rotors/', verbose_name="Rotor Image", null=True, blank=True)

    def __str__(self):
        return f"{self.brand} {self.series} {self.diameter} ({self.mount})"


class BrakeLever(BikeComponent):
    application = models.ForeignKey(Application, on_delete=models.CASCADE, verbose_name="Application")
    type = models.CharField(max_length=100, verbose_name="Type")
    actuation = models.ForeignKey(BrakeActuation, on_delete=models.PROTECT, verbose_name="Brake actuation type")
    mount = models.ForeignKey(HandlebarMount, on_delete=models.PROTECT, verbose_name="Lever mount type")
    material = models.ForeignKey(Material, on_delete=models.PROTECT, verbose_name="Material")
    lever_length = models.CharField(max_length=15, verbose_name="Lever length (-finger)")
    lever_side = models.CharField(max_length=10, verbose_name="Left or right")
    hose_connection = models.ForeignKey(BrakeHoseConnection, on_delete=models.PROTECT,
                                        verbose_name="Hose connection type")
    image = models.ImageField(upload_to='components/levers/', verbose_name="Brake lever Image", null=True, blank=True)

    def __str__(self):
        return f"{self.brand} {self.series} {self.type} {self.color}/{self.lever_side}"


class BrakeCaliper(BikeComponent):
    application = models.ForeignKey(Application, on_delete=models.CASCADE, verbose_name="Application")
    type = models.CharField(max_length=100, verbose_name="Type")
    actuation = models.ForeignKey(BrakeActuation, on_delete=models.PROTECT, verbose_name="Brake actuation type")
    mount = models.ForeignKey(BrakeMountStandard, on_delete=models.PROTECT, verbose_name="Caliper mount type")
    caliper_material = models.ForeignKey(Material, related_name="caliper_materials", on_delete=models.PROTECT,
                                         verbose_name="Caliper material")
    piston_material = models.ForeignKey(Material, related_name="piston_materials", on_delete=models.PROTECT,
                                        verbose_name="Piston material")
    hose_connection = models.ForeignKey(BrakeHoseConnection, on_delete=models.PROTECT,
                                        verbose_name="Hose connection type")
    brake_pads = models.ForeignKey(BrakePads, on_delete=models.PROTECT, verbose_name="Brake pads")
    image = models.ImageField(upload_to='components/calipers/', verbose_name="Brake caliper Image", null=True,
                              blank=True)

    def __str__(self):
        return f"{self.brand} {self.series} {self.type} {self.color}"


class Brakes(BikeComponent):
    application = models.ForeignKey(Application, on_delete=models.CASCADE, verbose_name="Application")
    type = models.CharField(max_length=100, verbose_name="Type")
    actuation = models.ForeignKey(BrakeActuation, on_delete=models.PROTECT, verbose_name="Brake actuation type")
    front_hose_length = models.IntegerField()
    caliper = models.ForeignKey(BrakeCaliper, on_delete=models.PROTECT, verbose_name="Brake caliper")
    lever = models.ForeignKey(BrakeLever, on_delete=models.PROTECT, verbose_name="Brake lever")
    brake_pads = models.ForeignKey(BrakePads, on_delete=models.PROTECT, verbose_name="Brake pads")

    def __str__(self):
        return f"{self.brand} {self.series} {self.type}"


class Rim(BikeComponent):
    wheel_size = models.ForeignKey(WheelSize, on_delete=models.PROTECT, verbose_name="Wheel size")
    spokes_num = models.IntegerField(verbose_name="Number of spokes")
    material = models.ForeignKey(Material, on_delete=models.PROTECT, verbose_name="Material")

    def __str__(self):
        return f"{self.brand} {self.series} {self.wheel_size}/{self.spokes_num}"


class DiskBrakeAdapter(BikeComponent):
    type = models.CharField(max_length=100, verbose_name="Type")
    material = models.ForeignKey(Material, on_delete=models.PROTECT, verbose_name="Material")
    rotor_size = models.ForeignKey(RotorDiameter, on_delete=models.PROTECT, verbose_name="Rotor size")
    mount = models.ForeignKey(BrakeMountStandard, related_name='diskbrakeadapter_mounts', on_delete=models.PROTECT,
                              verbose_name="Adapter mount type")
    caliper_mount = models.ForeignKey(BrakeMountStandard, related_name='diskbrakeadapter_caliper_mounts',
                                      on_delete=models.PROTECT, verbose_name="Caliper mount type")

    def __str__(self):
        return f"{self.brand} {self.series} ({self.mount} to {self.caliper_mount})"


class Hub(BikeComponent):
    application = models.ForeignKey(Application, on_delete=models.CASCADE, verbose_name="Application")
    material = models.ForeignKey(Material, on_delete=models.PROTECT, verbose_name="Material")
    spoke_holes = models.IntegerField(verbose_name="Number of spokes")
    rotor_mount = models.ForeignKey(RotorMountType, on_delete=models.PROTECT, verbose_name="Rotor mount type")
    axle_type = models.ForeignKey(AxleType, on_delete=models.PROTECT, verbose_name="Axle type")
    flange_distance = models.DecimalField(max_digits=3, decimal_places=1, verbose_name="Flange distance")
    partial_bolt_circle_diameter = models.DecimalField(max_digits=3, decimal_places=1,
                                                       verbose_name="Partial bolt_circle_diameter")
    color = models.CharField(max_length=50, verbose_name="Color")
    image = models.ImageField(upload_to='components/hubs/', verbose_name="Hub Image", null=True,
                              blank=True)

    class Meta:
        abstract = True


class FrontHub(Hub):
    def __str__(self):
        return f"{self.brand} {self.series} {self.axle_type}, Spokes - {self.spoke_holes}"


class RearHub(Hub):
    freehub = models.ForeignKey(FreehubStandard, on_delete=models.PROTECT, verbose_name="Freehub Standard")

    def __str__(self):
        return f"{self.brand} {self.series} {self.freehub}/{self.axle_type}, Spokes - {self.spoke_holes}"


class WheelLacing(models.Model):
    lacing_type = models.CharField(max_length=50, verbose_name="Wheel lacing type")

    def __str__(self):
        return self.lacing_type


class Wheel(BikeComponent):
    application = models.ForeignKey(Application, on_delete=models.CASCADE, verbose_name="Application")
    wheel_size = models.ForeignKey(WheelSize, on_delete=models.PROTECT, verbose_name="Wheel size")
    spokes_num = models.IntegerField(verbose_name="Number of spokes")
    rim = models.ForeignKey(Rim, on_delete=models.PROTECT, verbose_name="Rim")
    lacing = models.ForeignKey(WheelLacing, on_delete=models.PROTECT, verbose_name="Spokes lacing")
    rotor_mount = models.ForeignKey(RotorMountType, on_delete=models.PROTECT, verbose_name="Rotor mount type")
    tubeless_ready = models.BooleanField(verbose_name="Tubeless Ready")
    color = models.CharField(max_length=50, verbose_name="Color")

    class Meta:
        abstract = True


class FrontWheel(Wheel):
    front_hub = models.ForeignKey(FrontHub, on_delete=models.PROTECT, verbose_name="Front hub")

    def __str__(self):
        return f"{self.brand} {self.series} / {self.wheel_size} (Spokes - {self.spokes_num}) TLR:{self.tubeless_ready}"


class RearWheel(Wheel):
    rear_hub = models.ForeignKey(RearHub, on_delete=models.PROTECT, verbose_name="Rear hub")

    def __str__(self):
        return f"{self.brand} {self.series} / {self.wheel_size} (Spokes - {self.spokes_num}) TLR:{self.tubeless_ready}"


# class WheelSet(models.Model):
#     brand = models.ForeignKey(Brand, on_delete=models.CASCADE, verbose_name="Brand name")
#     series = models.CharField(max_length=100, verbose_name="Series Name")
#     application = models.ForeignKey(Application, on_delete=models.CASCADE, verbose_name="Application")
#     wheel_size = models.ForeignKey(WheelSize, on_delete=models.PROTECT, verbose_name="Wheel size")
#     # tyre_type = models.CharField()
#     spokes_num = models.IntegerField(verbose_name="Number of spokes")
#     rotor_mount = models.ForeignKey(RotorMountType, on_delete=models.PROTECT, verbose_name="Rotor mount type")
#     tubeless_ready = models.BooleanField(verbose_name="Tubeless Ready")
#     front_wheel = models.ForeignKey(FrontWheel, on_delete=models.PROTECT, verbose_name="Front wheel")
#     rear_wheel = models.ForeignKey(RearWheel, on_delete=models.PROTECT, verbose_name="Rear wheel")
#     weight_limit = models.IntegerField(verbose_name="Weight limit")
#
#     # color = models.CharField(max_length=50, verbose_name="Color")
#     features = models.TextField(verbose_name="Features", blank=True, null=True)
#     technology = models.TextField(verbose_name="Technology", blank=True, null=True)
#     weight = models.DecimalField(max_digits=5, decimal_places=3, verbose_name="Weight (kg)", null=True, blank=True)
#     price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Price (€)", null=True, blank=True)
#
#     def __str__(self):
#         return f"{self.brand} {self.series} / {self.wheel_size} TLR:{self.tubeless_ready}"


class WheelSet(BikeComponent):
    application = models.ForeignKey(Application, on_delete=models.CASCADE, verbose_name="Application")
    wheel_size = models.ForeignKey(WheelSize, on_delete=models.PROTECT, verbose_name="Wheel size")
    spokes_num = models.IntegerField(verbose_name="Number of spokes")
    rotor_mount = models.ForeignKey(RotorMountType, on_delete=models.PROTECT, verbose_name="Rotor mount type")
    tubeless_ready = models.BooleanField(verbose_name="Tubeless Ready")
    front_wheel = models.ForeignKey(FrontWheel, on_delete=models.PROTECT, verbose_name="Front wheel")
    rear_wheel = models.ForeignKey(RearWheel, on_delete=models.PROTECT, verbose_name="Rear wheel")
    weight_limit = models.IntegerField(verbose_name="Weight limit")

    def __str__(self):
        return f"{self.brand} {self.series} / {self.wheel_size} TLR:{self.tubeless_ready}"


class Bicycle(models.Model):
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE, verbose_name="Brand name")
    series = models.CharField(max_length=100, verbose_name="Series Name")
    frame = models.ForeignKey(Frame, on_delete=models.PROTECT, verbose_name="Frame")
    fork = models.ForeignKey(Fork, on_delete=models.PROTECT, verbose_name="Fork")
    wheelset = models.ForeignKey(WheelSet, on_delete=models.PROTECT, verbose_name="Wheel Set")
    drivetrain = models.ForeignKey(Drivetrain, on_delete=models.PROTECT, verbose_name="Drivetrain")
    brake = models.ForeignKey(Brakes, on_delete=models.PROTECT, verbose_name="Brake")
    # add rotors
    color = models.CharField(max_length=50, verbose_name="Color")
    weight = models.DecimalField(max_digits=5, decimal_places=3, verbose_name="Weight (kg)", null=True, blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Price (€)", null=True, blank=True)
    features = models.TextField(verbose_name="Features", blank=True, null=True)
    technology = models.TextField(verbose_name="Technology", blank=True, null=True)
    preview_image = models.ImageField(upload_to='bicycles/', verbose_name="Bicycle Image", null=True, blank=True)

    class Meta:
        abstract = True  # Робимо клас абстрактним, щоб не створювалася таблиця

    def __str__(self):
        return f"{self.brand} {self.series} ({self.__class__.__name__})"


class MTBBike(Bicycle):
    # suspension_type = models.ForeignKey(SuspensionType, on_delete=models.PROTECT, verbose_name="Suspension Type")
    handlebar = models.ForeignKey(HandlebarFlat, on_delete=models.PROTECT, verbose_name="Flat Bar")


class RoadBike(Bicycle):
    handlebar = models.ForeignKey(HandlebarDrop, on_delete=models.PROTECT, verbose_name="Drop Bar")


class GravelBike(Bicycle):
    handlebar = models.ForeignKey(HandlebarDrop, on_delete=models.PROTECT, verbose_name="Drop Bar")


class BicycleDetailedImage(models.Model):
    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    object_id = models.PositiveIntegerField()
    bicycle = GenericForeignKey('content_type', 'object_id')

    image = models.ImageField(upload_to='bicycles/detailed/', verbose_name="Detailed Bicycle Image")

    def __str__(self):
        return f"Detailed image for {self.bicycle}"


class BicycleConfigurator(models.Model):
    frame = models.ForeignKey(Frame, on_delete=models.PROTECT, verbose_name="Frame")
    fork = models.ForeignKey(Fork, on_delete=models.PROTECT, verbose_name="Fork")
    # Make wheelset or F/R wheel
    wheelset = models.ForeignKey(WheelSet, on_delete=models.PROTECT, verbose_name="Wheel Set")
    # Drivetrain
    crankset = models.ForeignKey(Crankset, on_delete=models.PROTECT, verbose_name="Crankset")
    bottom_bracket = models.ForeignKey(BottomBracket, on_delete=models.PROTECT, verbose_name="Bottom Bracket")
    cassette = models.ForeignKey(Cassette, on_delete=models.PROTECT, verbose_name="Cassette")
    chain = models.ForeignKey(Chain, on_delete=models.PROTECT, verbose_name="Chain")
    derailleur = models.ForeignKey(Derailleur, on_delete=models.PROTECT, verbose_name="Rear Derailleur")
    front_derailleur = models.ForeignKey(FrontDerailleur, on_delete=models.PROTECT, verbose_name="Front Derailleur",
                                         null=True, blank=True)
    # Brake or custom
    brake = models.ForeignKey(Brakes, on_delete=models.PROTECT, verbose_name="Brake")
    # Custom brakes

    front_rotor = models.ForeignKey(BrakeRotor, on_delete=models.PROTECT, verbose_name="Front Rotor",
                                    related_name='front_rotor_configurations', null=True,
                                    blank=True)
    rear_rotor = models.ForeignKey(BrakeRotor, on_delete=models.PROTECT, verbose_name="Rear Rotor",
                                   related_name='rear_rotor_configurations', null=True,
                                   blank=True)
    rear_shifter = models.ForeignKey(Shifter, on_delete=models.PROTECT, related_name='front_shifter_configurations',
                                     verbose_name="Rear Shifter")
    front_shifter = models.ForeignKey(Shifter, on_delete=models.PROTECT, related_name='rear_shifter_configurations',
                                      verbose_name="Front Shifter", null=True,
                                      blank=True)
    weight = models.DecimalField(max_digits=5, decimal_places=3, verbose_name="Weight (kg)", null=True, blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Price (€)", null=True, blank=True)
    preview_image = models.ImageField(upload_to='bicycles/', verbose_name="Bicycle Image", null=True, blank=True)

    def save(self, *args, **kwargs):
        # Calculate total weight and price before saving
        components = [
            self.frame, self.fork, self.wheelset,
            self.crankset, self.bottom_bracket, self.cassette,
            self.chain, self.derailleur, self.brake, self.rear_shifter
        ]

        # front derailleur, front and rear rotors, front shifter are optional
        optional_components = [self.front_derailleur, self.front_rotor, self.rear_rotor, self.front_shifter]

        total_weight = 0
        total_price = 0

        for component in components + optional_components:
            if component:  # if it's not None
                total_weight += component.weight or 0
                total_price += component.price or 0

        self.weight = total_weight
        self.price = total_price

        super().save(*args, **kwargs)

    # сделать более детальную
    class Meta:
        abstract = True  # Робимо клас абстрактним, щоб не створювалася таблиця


class MTBBicycleConfiguration(BicycleConfigurator):
    name = models.CharField(max_length=25, verbose_name="Bicycle configuration name")
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f"Configured {self.name} - {self.id} ({self.__class__.__name__})"


class Order(models.Model):
    user = models.ForeignKey('User', related_name='orders', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=20, choices=[('pending', 'Pending'), ('completed', 'Completed')],
                              default='pending')
    total_price = models.DecimalField(max_digits=10, decimal_places=2)
    shipping_address = models.TextField()

    def __str__(self):
        return f"Order {self.id} - {self.user.first_name} {self.user.last_name}"

    def calculate_total_price(self):
        order_items = self.order_items.all()
        return sum([item.calculate_item_price() for item in order_items])


class OrderItem(models.Model):
    order = models.ForeignKey(Order, related_name='order_items', on_delete=models.CASCADE)
    bicycle = models.ForeignKey(MTBBike, null=True, blank=True, on_delete=models.SET_NULL)
    bicycle_configurator = models.ForeignKey(MTBBicycleConfiguration, null=True, blank=True, on_delete=models.SET_NULL)
    quantity = models.PositiveIntegerField(default=1)
    price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"Item {self.id} - {self.bicycle or self.bicycle_configurator}"

    def calculate_item_price(self):
        return self.quantity * self.price

# class Order(models.Model):
#     first_name = models.CharField(max_length=50, verbose_name="First Name")
#     last_name = models.CharField(max_length=50, verbose_name="Last Name")
#     email = models.EmailField(verbose_name="Email Address")
#     phone = models.CharField(max_length=20, verbose_name="Phone Number")
#     datetime = models.DateTimeField(auto_now_add=True, verbose_name="Order Date")
#
#     def __str__(self):
#         return f"Order №{self.id} by {self.first_name} {self.last_name}"
#
#     @property
#     def total_price(self):
#         return sum(item.total_price for item in self.items.all())
#
#
# class OrderItem(models.Model):
#     order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name="items")
#     case = models.ForeignKey(Case, on_delete=models.CASCADE)
#     quantity = models.PositiveIntegerField(default=1)
#
#     def __str__(self):
#         return f"{self.quantity} x {self.case.name}"
#
#     @property
#     def total_price(self):
#         return self.quantity * self.case.price

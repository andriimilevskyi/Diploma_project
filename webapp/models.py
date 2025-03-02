from django.db import models


# Create your models here.


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
    name = models.CharField(max_length=100, verbose_name="Brand Name")

    def __str__(self):
        return self.name


class Application(models.Model):
    name = models.CharField(max_length=100, verbose_name="Application name")

    def __str__(self):
        return self.name


class Material(models.Model):
    material_name = models.CharField(max_length=50, verbose_name="Material")

    def __str__(self):
        return self.material_name


class WheelSize(models.Model):
    size = models.CharField(max_length=15, verbose_name="Wheel Size")

    def __str__(self):
        return self.size


class TyreSize(models.Model):
    size = models.CharField(max_length=15, verbose_name="Tyre Size")

    def __str__(self):
        return self.size


class AxleType(models.Model):
    type = models.CharField(max_length=15, verbose_name="Axle type")
    diameter = models.IntegerField(verbose_name="Axle diameter")
    length = models.IntegerField(verbose_name="Axle length")
    side = models.CharField(max_length=15, verbose_name="Axle side")

    def __str__(self):
        return f"{self.side}/{self.type}, {self.diameter}mm/{self.length}mm"


class BBStandard(models.Model):
    name = models.CharField(max_length=15, verbose_name="Bottom Bracket standard name")
    type = models.CharField(max_length=15, verbose_name="Bottom Bracket standard type")

    def __str__(self):
        return f"{self.type}/{self.name}"


class FrontDerailleurMount(models.Model):
    name = models.CharField(max_length=15, verbose_name="Front Derailleur Mount standard name")
    type = models.CharField(max_length=15, verbose_name="Front Derailleur Mount standard type", null=True, blank=True)

    def __str__(self):
        return f"{self.name}, {self.type}"


class RotorDiameter(models.Model):
    diameter = models.IntegerField(verbose_name="Rotor diameter")

    def __str__(self):
        return f"{self.diameter}mm"


class RotorMountType(models.Model):
    mount_type = models.CharField(max_length=50, verbose_name="Rotor Mount Type")

    def __str__(self):
        return self.mount_type


class BrakeMountStandard(models.Model):
    name = models.CharField(max_length=50, verbose_name="Brake Mount standard name")
    rotor_size = models.ForeignKey(RotorDiameter, verbose_name="Rotor size in mm", on_delete=models.PROTECT, null=True,
                                   blank=True)

    def __str__(self):
        return f"{self.name} ({self.rotor_size})" if self.rotor_size else f"{self.name}"


class TubeDiameter(models.Model):
    diameter = models.DecimalField(max_digits=3, decimal_places=1, verbose_name="Diameter of tube for Stem")

    def __str__(self):
        return f"{self.diameter}"


class Frame(models.Model):
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE, verbose_name="Brand name")
    series = models.CharField(max_length=100, verbose_name="Series Name")
    application = models.ForeignKey(Application, on_delete=models.CASCADE, verbose_name="Application")
    type = models.CharField(max_length=100, verbose_name="Type")
    wheel_size = models.ForeignKey(WheelSize, on_delete=models.PROTECT)
    tyre_size = models.ForeignKey(TyreSize, on_delete=models.PROTECT, verbose_name="Max Tyre size")
    axle_type = models.ForeignKey(AxleType, on_delete=models.PROTECT, verbose_name="Axle type")
    size = models.CharField(max_length=50, verbose_name="Size")
    seatpost = models.IntegerField(verbose_name="Seatpost")
    min_rider_height = models.DecimalField(max_digits=4, decimal_places=1, verbose_name="Minimal Rider Height (cm)",
                                           null=True,
                                           blank=True)
    max_rider_height = models.DecimalField(max_digits=4, decimal_places=1, verbose_name="Maximal Rider Height (cm)",
                                           null=True,
                                           blank=True)
    bb_standard = models.ForeignKey(BBStandard, on_delete=models.PROTECT, verbose_name="Bottom Bracket Standard")
    fork_travel = models.IntegerField(verbose_name="Fork Travel")
    front_derailleur_mount = models.ForeignKey(FrontDerailleurMount, on_delete=models.PROTECT,
                                               verbose_name="Front Derailleur Mount", null=True,
                                               blank=True)
    brake_mount = models.ForeignKey(BrakeMountStandard, on_delete=models.PROTECT, verbose_name="Brake Mount")
    chainring_size_max = models.CharField(max_length=50, verbose_name="Max Chainring Size")
    material = models.ForeignKey(Material, on_delete=models.PROTECT, verbose_name="Material")
    features = models.TextField(verbose_name="Features", blank=True, null=True)
    technology = models.TextField(verbose_name="Technology", blank=True, null=True)
    color = models.CharField(max_length=50, verbose_name="Color")
    weight = models.DecimalField(max_digits=5, decimal_places=3, verbose_name="Weight (kg)", null=True, blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Price (€)", null=True, blank=True)
    image = models.ImageField(upload_to='components/frames/', verbose_name="Frame Image", null=True, blank=True)

    def __str__(self):
        return f"{self.brand.name} {self.series} ({self.size}, {self.seatpost}) - {self.type}"


class Fork(models.Model):
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE, verbose_name="Brand name")
    series = models.CharField(max_length=100, verbose_name="Series Name")
    application = models.ForeignKey(Application, on_delete=models.CASCADE, verbose_name="Application")
    type = models.CharField(max_length=100, verbose_name="Type")
    wheel_size = models.ForeignKey(WheelSize, on_delete=models.CASCADE)
    suspension_type = models.CharField(max_length=100, verbose_name="Suspension type")
    stem_diameter = models.ForeignKey(TubeDiameter, on_delete=models.PROTECT,
                                      verbose_name="Steerer Tube Diameter (Stem)")
    travel = models.IntegerField(verbose_name="Fork Travel in mm")
    offset = models.IntegerField(verbose_name="Offset in mm")
    axle_type = models.ForeignKey(AxleType, on_delete=models.CASCADE, verbose_name="Axle type")
    brake_mount = models.ForeignKey(BrakeMountStandard, on_delete=models.PROTECT, verbose_name="Brake Mount")
    remote = models.BooleanField(verbose_name="Remote control")
    tyre_size = models.ForeignKey(TyreSize, on_delete=models.CASCADE, verbose_name="Max Tyre size")
    rotor_size_max = models.ForeignKey(RotorDiameter, on_delete=models.PROTECT, verbose_name="Max Rotor size")
    material = models.ForeignKey(Material, on_delete=models.PROTECT, verbose_name="Material")
    features = models.TextField(verbose_name="Features", blank=True, null=True)
    technology = models.TextField(verbose_name="Technology", blank=True, null=True)
    color = models.CharField(max_length=50, verbose_name="Color")
    weight = models.DecimalField(max_digits=5, decimal_places=3, verbose_name="Weight (kg)", null=True, blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Price (€)", null=True, blank=True)
    image = models.ImageField(upload_to='components/forks/', verbose_name="Fork Image", null=True, blank=True)

    def __str__(self):
        return f"{self.brand} {self.series} {self.wheel_size} {self.travel}mm/{self.suspension_type}"


class HandlebarMTB(models.Model):
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE, verbose_name="Brand name")
    series = models.CharField(max_length=100, verbose_name="Series Name")
    application = models.ForeignKey(Application, on_delete=models.CASCADE, verbose_name="Application")
    width = models.IntegerField(verbose_name="Handlebar width (mm)")
    stem_clamp = models.ForeignKey(TubeDiameter, on_delete=models.PROTECT, verbose_name="Stem (Handlebar) clamp size")
    # rise = models.DecimalField(max_digits=2, decimal_places=1,verbose_name="Handlebar rise")
    rise = models.IntegerField(verbose_name="Handlebar rise")
    backsweep = models.IntegerField(verbose_name="Handlebar backsweep (°)")
    upsweep = models.IntegerField(verbose_name="Handlebar upsweep (°)")
    material = models.ForeignKey(Material, on_delete=models.PROTECT, verbose_name="Material")
    features = models.TextField(verbose_name="Features", blank=True, null=True)
    technology = models.TextField(verbose_name="Technology", blank=True, null=True)
    color = models.CharField(max_length=50, verbose_name="Color")
    weight = models.DecimalField(max_digits=5, decimal_places=3, verbose_name="Weight (kg)", null=True, blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Price (€)", null=True, blank=True)
    image = models.ImageField(upload_to='components/handlebars/', verbose_name="HandlebarMTB Image", null=True,
                              blank=True)

    def __str__(self):
        return f"{self.brand} {self.series} {self.width}mm ({self.stem_clamp}mm"


class HandlebarRoad(models.Model):
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE, verbose_name="Brand name")
    series = models.CharField(max_length=100, verbose_name="Series Name")
    application = models.ForeignKey(Application, on_delete=models.CASCADE, verbose_name="Application")
    width = models.IntegerField(verbose_name="Handlebar width in mm (center-to-center)")
    stem_clamp = models.ForeignKey(TubeDiameter, on_delete=models.PROTECT, verbose_name="Stem (Handlebar) clamp size")
    drop = models.IntegerField(verbose_name="Handlebar drop")
    reach = models.IntegerField(verbose_name="Handlebar reach")
    flare = models.IntegerField(verbose_name="Handlebar upsweep (°)")
    internal_cable_routing = models.BooleanField(verbose_name="Internal cable routing")
    material = models.ForeignKey(Material, on_delete=models.PROTECT, verbose_name="Material")
    features = models.TextField(verbose_name="Features", blank=True, null=True)
    technology = models.TextField(verbose_name="Technology", blank=True, null=True)
    color = models.CharField(max_length=50, verbose_name="Color")
    weight = models.DecimalField(max_digits=5, decimal_places=3, verbose_name="Weight (kg)", null=True, blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Price (€)", null=True, blank=True)
    image = models.ImageField(upload_to='components/handlebars/', verbose_name="HandlebarRoad Image", null=True,
                              blank=True)

    def __str__(self):
        return f"{self.brand} {self.series} {self.width}mm ({self.stem_clamp}mm"


class Stem(models.Model):
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE, verbose_name="Brand name")
    series = models.CharField(max_length=100, verbose_name="Series Name")
    application = models.ForeignKey(Application, on_delete=models.CASCADE, verbose_name="Application")
    steerer_clamp = models.ForeignKey(TubeDiameter, related_name='steerer_clamp_stems', on_delete=models.PROTECT,
                                      verbose_name="Steerer Tube Diameter (Stem)")
    handlebar_clamp = models.ForeignKey(TubeDiameter, related_name='handlebar_clamp_stems', on_delete=models.PROTECT,
                                        verbose_name="Stem (Handlebar) clamp size")
    length = models.IntegerField(verbose_name="Stem length (mm)")
    angle = models.IntegerField(verbose_name="Stem andle degree (°)")
    stack_height = models.IntegerField(verbose_name="Stack height")
    material = models.ForeignKey(Material, on_delete=models.PROTECT, verbose_name="Material")
    features = models.TextField(verbose_name="Features", blank=True, null=True)
    technology = models.TextField(verbose_name="Technology", blank=True, null=True)
    color = models.CharField(max_length=50, verbose_name="Color")
    weight = models.DecimalField(max_digits=5, decimal_places=3, verbose_name="Weight (kg)", null=True, blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Price (€)", null=True, blank=True)
    image = models.ImageField(upload_to='components/stems/', verbose_name="Stem Image", null=True,
                              blank=True)

    def __str__(self):
        return f"{self.brand} {self.series} {self.material} ({self.length}mm/{self.angle}°)"


class ChainringMountStandard(models.Model):
    type = models.CharField(max_length=100, verbose_name="Chainring mount standard type")

    def __str__(self):
        return self.type


class Crankset(models.Model):
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE, verbose_name="Brand name")
    series = models.CharField(max_length=100, verbose_name="Series Name")
    application = models.ForeignKey(Application, on_delete=models.CASCADE, verbose_name="Application")
    chainring_mount = models.ForeignKey(ChainringMountStandard, on_delete=models.PROTECT,
                                        verbose_name="Chainring Mount Standard")
    gradation = models.CharField(max_length=15, verbose_name="Chainrings gradation (smallest-biggest)T")
    gearing = models.IntegerField(verbose_name="Gears count (x-speed)")
    crank_arm_length = models.DecimalField(max_digits=3, decimal_places=1, verbose_name="Crank Arm length")
    axle_diameter = models.IntegerField(verbose_name="Axle diameter in mm")
    chainline = models.DecimalField(max_digits=2, decimal_places=1, verbose_name="Chainline in mm", null=True)
    bb_standard = models.ForeignKey(BBStandard, on_delete=models.PROTECT, verbose_name="Bottom Bracket standard")
    material = models.ForeignKey(Material, on_delete=models.PROTECT, verbose_name="Material")
    features = models.TextField(verbose_name="Features", blank=True, null=True)
    technology = models.TextField(verbose_name="Technology", blank=True, null=True)
    color = models.CharField(max_length=50, verbose_name="Color")
    weight = models.DecimalField(max_digits=5, decimal_places=3, verbose_name="Weight (kg)", null=True, blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Price (€)", null=True, blank=True)
    image = models.ImageField(upload_to='components/cranks/', verbose_name="Cranks Image", null=True,
                              blank=True)

    def __str__(self):
        return f"{self.brand} {self.series} {self.gearing} {self.gradation} {self.chainring_mount}"


class BottomBracket(models.Model):
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE, verbose_name="Brand name")
    series = models.CharField(max_length=100, verbose_name="Series Name")
    application = models.ForeignKey(Application, on_delete=models.CASCADE, verbose_name="Application")
    type = models.CharField(max_length=100, verbose_name="Type")
    shell_width = models.IntegerField(verbose_name="Shell width in mm")
    axle_diameter = models.IntegerField(verbose_name="Axle diameter in mm")
    features = models.TextField(verbose_name="Features", blank=True, null=True)
    technology = models.TextField(verbose_name="Technology", blank=True, null=True)
    color = models.CharField(max_length=50, verbose_name="Color")
    weight = models.DecimalField(max_digits=5, decimal_places=3, verbose_name="Weight (kg)", null=True, blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Price (€)", null=True, blank=True)
    image = models.ImageField(upload_to='components/bottom_brackets/', verbose_name="BottomBracket Image", null=True,
                              blank=True)

    def __str__(self):
        return f"{self.brand} {self.series} {self.type}"


class FreehubStandard(models.Model):
    freehub_name = models.CharField(max_length=50, verbose_name="Freehub standard")

    def __str__(self):
        return self.freehub_name


class Cassette(models.Model):
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE, verbose_name="Brand name")
    series = models.CharField(max_length=100, verbose_name="Series Name")
    application = models.ForeignKey(Application, on_delete=models.CASCADE, verbose_name="Application")
    gearing = models.IntegerField(verbose_name="Gears count (x-speed)")
    gradation = models.CharField(max_length=10, verbose_name="Gradation (smallest-biggest)")
    gradation_all = models.CharField(max_length=100, verbose_name="All gradation", null=True)
    smallest_gear = models.IntegerField(verbose_name="Smallest star")
    biggest_gear = models.IntegerField(verbose_name="Biggest star")
    material = models.ForeignKey(Material, on_delete=models.PROTECT, verbose_name="Material")
    features = models.TextField(verbose_name="Features", blank=True, null=True)
    technology = models.TextField(verbose_name="Technology", blank=True, null=True)
    freehub_standard = models.ForeignKey(FreehubStandard, on_delete=models.PROTECT, verbose_name="Freehub standard")
    color = models.CharField(max_length=50, verbose_name="Color")
    weight = models.DecimalField(max_digits=5, decimal_places=3, verbose_name="Weight (kg)", null=True, blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Price (€)", null=True, blank=True)
    image = models.ImageField(upload_to='components/cassettes/', verbose_name="Cassette Image", null=True,
                              blank=True)

    def __str__(self):
        return f"{self.brand} {self.series} {self.gearing} ({self.gradation}, {self.freehub_standard})"


class Chain(models.Model):
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE, verbose_name="Brand name")
    series = models.CharField(max_length=100, verbose_name="Series Name")
    links_num = models.IntegerField(verbose_name="Number of links")
    gearing = models.IntegerField(verbose_name="Gears count (x-speed)")
    application = models.ForeignKey(Application, on_delete=models.CASCADE, verbose_name="Application")
    clousing_type = models.CharField(max_length=15, verbose_name="Chain closing type")
    directional = models.BooleanField(verbose_name="Directional chain")
    material = models.ForeignKey(Material, on_delete=models.PROTECT, verbose_name="Material")
    features = models.TextField(verbose_name="Features", blank=True, null=True)
    technology = models.TextField(verbose_name="Technology", blank=True, null=True)
    color = models.CharField(max_length=50, verbose_name="Color")
    weight = models.DecimalField(max_digits=5, decimal_places=3, verbose_name="Weight (kg)", null=True, blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Price (€)", null=True, blank=True)
    image = models.ImageField(upload_to='components/chains/', verbose_name="Chain Image", null=True,
                              blank=True)

    def __str__(self):
        return f"{self.brand} {self.series} {self.gearing}"


class Derailleur(models.Model):
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE, verbose_name="Brand name")
    series = models.CharField(max_length=100, verbose_name="Series Name")
    gearing = models.IntegerField(verbose_name="Gears count (x-speed)")
    type = models.CharField(max_length=100, verbose_name="Type")
    application = models.ForeignKey(Application, on_delete=models.CASCADE, verbose_name="Application")
    smallest_gear = models.IntegerField(verbose_name="Smallest star compatible")
    biggest_gear = models.IntegerField(verbose_name="Biggest star compatible")
    material = models.ForeignKey(Material, on_delete=models.PROTECT, verbose_name="Material")
    features = models.TextField(verbose_name="Features", blank=True, null=True)
    technology = models.TextField(verbose_name="Technology", blank=True, null=True)
    color = models.CharField(max_length=50, verbose_name="Color")
    weight = models.DecimalField(max_digits=5, decimal_places=3, verbose_name="Weight (kg)", null=True, blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Price (€)", null=True, blank=True)
    image = models.ImageField(upload_to='components/dirailleurs/', verbose_name="Dirailleur Image", null=True,
                              blank=True)

    def __str__(self):
        return f"{self.brand} {self.series} {self.gearing}"


class FrontDerailleur(models.Model):
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE, verbose_name="Brand name")
    series = models.CharField(max_length=100, verbose_name="Series Name")
    gearing = models.IntegerField(verbose_name="Gears count (x-speed)")
    type = models.CharField(max_length=100, verbose_name="Type")
    application = models.ForeignKey(Application, on_delete=models.CASCADE, verbose_name="Application")
    chainline = models.DecimalField(max_digits=2, decimal_places=1, verbose_name="Chainline in mm")
    chainring_size_max = models.CharField(max_length=50, verbose_name="Max Chainring Size")
    capacity = models.IntegerField(verbose_name="Capacity (x-tooth)")
    material = models.ForeignKey(Material, on_delete=models.PROTECT, verbose_name="Material")
    features = models.TextField(verbose_name="Features", blank=True, null=True)
    technology = models.TextField(verbose_name="Technology", blank=True, null=True)
    mount = models.ForeignKey(FrontDerailleurMount, on_delete=models.PROTECT, verbose_name="Front Derailleur Mount")
    color = models.CharField(max_length=50, verbose_name="Color")
    weight = models.DecimalField(max_digits=5, decimal_places=3, verbose_name="Weight (kg)", null=True, blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Price (€)", null=True, blank=True)
    image = models.ImageField(upload_to='components/front_derailleurs/', verbose_name="Front derailleur Image",
                              null=True,
                              blank=True)

    def __str__(self):
        return f"{self.brand} {self.series} {self.gearing}"


class HandlebarMount(models.Model):
    mount_standard = models.CharField(max_length=50, verbose_name="Handlebar mount type")

    def __str__(self):
        return self.mount_standard


class Shifter(models.Model):
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE, verbose_name="Brand name")
    series = models.CharField(max_length=100, verbose_name="Series Name")
    gearing = models.IntegerField(verbose_name="Gears count (x-speed)")
    type = models.CharField(max_length=100, verbose_name="Type")
    application = models.ForeignKey(Application, on_delete=models.CASCADE, verbose_name="Application")
    mount = models.ForeignKey(HandlebarMount, on_delete=models.PROTECT, verbose_name="Mount type")
    material = models.ForeignKey(Material, on_delete=models.PROTECT, verbose_name="Material")
    features = models.TextField(verbose_name="Features", blank=True, null=True)
    technology = models.TextField(verbose_name="Technology", blank=True, null=True)
    color = models.CharField(max_length=50, verbose_name="Color")
    weight = models.DecimalField(max_digits=5, decimal_places=3, verbose_name="Weight (kg)", null=True, blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Price (€)", null=True, blank=True)
    image = models.ImageField(upload_to='components/shifters/', verbose_name="Shifter Image", null=True, blank=True)

    def __str__(self):
        return f"{self.brand} {self.series} {self.gearing}"


class BrakePadsCompound(models.Model):
    compound_type = models.CharField(max_length=15, verbose_name="Pads compound material")

    def __str__(self):
        return self.compound_type


class BrakeHoseConnection(models.Model):
    connection_type = models.CharField(max_length=15, verbose_name="Brake hose connection type")

    def __str__(self):
        return self.connection_type


class BrakePads(models.Model):
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE, verbose_name="Brand name")
    series = models.CharField(max_length=100, verbose_name="Series Name")
    compound = models.ForeignKey(BrakePadsCompound, on_delete=models.PROTECT, verbose_name="Compound type")
    plate_material = models.ForeignKey(Material, on_delete=models.PROTECT, verbose_name="Plate material")
    cooling_fins = models.BooleanField(verbose_name="Cooling fins")
    features = models.TextField(verbose_name="Features", blank=True, null=True)
    technology = models.TextField(verbose_name="Technology", blank=True, null=True)
    weight = models.DecimalField(max_digits=5, decimal_places=3, verbose_name="Weight (kg)", null=True, blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Price (€)", null=True, blank=True)
    image = models.ImageField(upload_to='components/brake_pads/', verbose_name="Brake pads Image", null=True,
                              blank=True)

    def __str__(self):
        return f"{self.brand} {self.series} {self.compound}"


class BrakeActuation(models.Model):
    actuation_type = models.CharField(max_length=15, verbose_name="Brake actuation type")

    def __str__(self):
        return self.actuation_type


class BrakeRotor(models.Model):
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE, verbose_name="Brand name")
    series = models.CharField(max_length=100, verbose_name="Series Name")
    mount = models.ForeignKey(RotorMountType, on_delete=models.PROTECT, verbose_name="Mount type")
    diameter = models.ForeignKey(RotorDiameter, on_delete=models.PROTECT, verbose_name="Rotor diameter")
    features = models.TextField(verbose_name="Features", blank=True, null=True)
    technology = models.TextField(verbose_name="Technology", blank=True, null=True)
    actuation = models.ForeignKey(BrakeActuation, on_delete=models.PROTECT, verbose_name="Brake actuation type")
    # brake_pads = models.ForeignKey(Brake_Pads, on_delete=models.PROTECT, verbose_name="Brake pads")
    color = models.CharField(max_length=50, verbose_name="Color")
    weight = models.DecimalField(max_digits=5, decimal_places=3, verbose_name="Weight (kg)", null=True, blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Price (€)", null=True, blank=True)
    image = models.ImageField(upload_to='components/rotors/', verbose_name="Rotor Image", null=True, blank=True)

    def __str__(self):
        return f"{self.brand} {self.series} {self.diameter} ({self.mount})"


class BrakeLever(models.Model):
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE, verbose_name="Brand name")
    series = models.CharField(max_length=100, verbose_name="Series Name")
    application = models.ForeignKey(Application, on_delete=models.CASCADE, verbose_name="Application")
    type = models.CharField(max_length=100, verbose_name="Type")
    actuation = models.ForeignKey(BrakeActuation, on_delete=models.PROTECT, verbose_name="Brake actuation type")
    mount = models.ForeignKey(HandlebarMount, on_delete=models.PROTECT, verbose_name="Lever mount type")
    material = models.ForeignKey(Material, on_delete=models.PROTECT, verbose_name="Material")
    lever_length = models.CharField(max_length=15, verbose_name="Lever length (-finger)")
    lever_side = models.CharField(max_length=10, verbose_name="Left or right")
    hose_connection = models.ForeignKey(BrakeHoseConnection, on_delete=models.PROTECT,
                                        verbose_name="Hose connection type")
    color = models.CharField(max_length=50, verbose_name="Color")
    features = models.TextField(verbose_name="Features", blank=True, null=True)
    technology = models.TextField(verbose_name="Technology", blank=True, null=True)
    weight = models.DecimalField(max_digits=5, decimal_places=3, verbose_name="Weight (kg)", null=True, blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Price (€)", null=True, blank=True)
    image = models.ImageField(upload_to='components/levers/', verbose_name="Brake lever Image", null=True, blank=True)

    def __str__(self):
        return f"{self.brand} {self.series} {self.type} {self.color}/{self.lever_side}"


class BrakeCaliper(models.Model):
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE, verbose_name="Brand name")
    series = models.CharField(max_length=100, verbose_name="Series Name")
    application = models.ForeignKey(Application, on_delete=models.CASCADE, verbose_name="Application")
    type = models.CharField(max_length=100, verbose_name="Type")
    actuation = models.ForeignKey(BrakeActuation, on_delete=models.PROTECT, verbose_name="Brake actuation type")
    mount = models.ForeignKey(BrakeMountStandard, on_delete=models.PROTECT, verbose_name="Caliper mount type")
    # mounting_position = models.CharField() #front or back
    caliper_material = models.ForeignKey(Material, related_name="caliper_materials", on_delete=models.PROTECT,
                                         verbose_name="Caliper material")
    piston_material = models.ForeignKey(Material, related_name="piston_materials", on_delete=models.PROTECT,
                                        verbose_name="Piston material")
    hose_connection = models.ForeignKey(BrakeHoseConnection, on_delete=models.PROTECT,
                                        verbose_name="Hose connection type")
    brake_pads = models.ForeignKey(BrakePads, on_delete=models.PROTECT, verbose_name="Brake pads")
    # rotor_compatibility = models.CharField()
    color = models.CharField(max_length=50, verbose_name="Color")
    features = models.TextField(verbose_name="Features", blank=True, null=True)
    technology = models.TextField(verbose_name="Technology", blank=True, null=True)
    weight = models.DecimalField(max_digits=5, decimal_places=3, verbose_name="Weight (kg)", null=True, blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Price (€)", null=True, blank=True)
    image = models.ImageField(upload_to='components/calipers/', verbose_name="Brake caliper Image", null=True,
                              blank=True)

    def __str__(self):
        return f"{self.brand} {self.series} {self.type} {self.color}"


class Brakes(models.Model):
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE, verbose_name="Brand name")
    series = models.CharField(max_length=100, verbose_name="Series Name")
    application = models.ForeignKey(Application, on_delete=models.CASCADE, verbose_name="Application")
    type = models.CharField(max_length=100, verbose_name="Type")
    actuation = models.ForeignKey(BrakeActuation, on_delete=models.PROTECT, verbose_name="Brake actuation type")
    front_hose_length = models.IntegerField()
    caliper = models.ForeignKey(BrakeCaliper, on_delete=models.PROTECT, verbose_name="Brake caliper")
    lever = models.ForeignKey(BrakeLever, on_delete=models.PROTECT, verbose_name="Brake lever")
    brake_pads = models.ForeignKey(BrakePads, on_delete=models.PROTECT, verbose_name="Brake pads")
    features = models.TextField(verbose_name="Features", blank=True, null=True)
    technology = models.TextField(verbose_name="Technology", blank=True, null=True)
    color = models.CharField(max_length=50, verbose_name="Color")
    weight = models.DecimalField(max_digits=5, decimal_places=3, verbose_name="Weight (kg)", null=True, blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Price (€)", null=True, blank=True)

    def __str__(self):
        return f"{self.brand} {self.series} {self.type}"


class DiskBrakeAdapter(models.Model):
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE, verbose_name="Brand name")
    series = models.CharField(max_length=100, verbose_name="Series Name")
    type = models.CharField(max_length=100, verbose_name="Type")
    material = models.ForeignKey(Material, on_delete=models.PROTECT, verbose_name="Material")
    rotor_size = models.ForeignKey(RotorDiameter, on_delete=models.PROTECT, verbose_name="Rotor size")
    mount = models.ForeignKey(BrakeMountStandard, related_name='diskbrakeadapter_mounts', on_delete=models.PROTECT,
                              verbose_name="Adapter mount type")
    caliper_mount = models.ForeignKey(BrakeMountStandard, related_name='diskbrakeadapter_caliper_mounts',
                                      on_delete=models.PROTECT, verbose_name="Caliper mount type")
    color = models.CharField(max_length=50, verbose_name="Color")
    weight = models.DecimalField(max_digits=5, decimal_places=3, verbose_name="Weight (kg)", null=True, blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Price (€)", null=True, blank=True)

    def __str__(self):
        return f"{self.brand} {self.series} ({self.mount} to {self.caliper_mount})"


class Rim(models.Model):
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE, verbose_name="Brand name")
    series = models.CharField(max_length=100, verbose_name="Series Name")
    wheel_size = models.ForeignKey(WheelSize, on_delete=models.PROTECT, verbose_name="Wheel size")
    spokes_num = models.IntegerField(verbose_name="Number of spokes")
    # tyre_type = models.CharField()
    material = models.ForeignKey(Material, on_delete=models.PROTECT, verbose_name="Material")
    features = models.TextField(verbose_name="Features", blank=True, null=True)
    technology = models.TextField(verbose_name="Technology", blank=True, null=True)
    weight = models.DecimalField(max_digits=5, decimal_places=3, verbose_name="Weight (kg)", null=True, blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Price (€)", null=True, blank=True)
    image = models.ImageField(upload_to='components/rims/', verbose_name="Rim Image", null=True, blank=True)

    # add rims brakes
    def __str__(self):
        return f"{self.brand} {self.series} {self.wheel_size}/{self.spokes_num}"


class FrontHub(models.Model):
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE, verbose_name="Brand name")
    series = models.CharField(max_length=100, verbose_name="Series Name")
    application = models.ForeignKey(Application, on_delete=models.CASCADE, verbose_name="Application")
    material = models.ForeignKey(Material, on_delete=models.PROTECT, verbose_name="Material")
    # bearings = models.CharField()
    spoke_holes = models.IntegerField(verbose_name="Number of spokes")
    rotor_mount = models.ForeignKey(RotorMountType, on_delete=models.PROTECT, verbose_name="Rotor mount type")
    axle_type = models.ForeignKey(AxleType, on_delete=models.PROTECT, verbose_name="Axle type")
    flange_distance = models.DecimalField(max_digits=3, decimal_places=1, verbose_name="Flange distance")
    partial_bolt_circle_diameter = models.DecimalField(max_digits=3, decimal_places=1,
                                                       verbose_name="Partial bolt_circle_diameter")
    # spoke_hole_diameter = models.CharField()
    features = models.TextField(verbose_name="Features", blank=True, null=True)
    technology = models.TextField(verbose_name="Technology", blank=True, null=True)
    color = models.CharField(max_length=50, verbose_name="Color")
    weight = models.DecimalField(max_digits=5, decimal_places=3, verbose_name="Weight (kg)", null=True, blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Price (€)", null=True, blank=True)
    image = models.ImageField(upload_to='components/hubs/', verbose_name="Front hub Image", null=True, blank=True)

    def __str__(self):
        return f"{self.brand} {self.series} {self.axle_type}, Spokes - {self.spoke_holes}"


class RearHub(models.Model):
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE, verbose_name="Brand name")
    series = models.CharField(max_length=100, verbose_name="Series Name")
    application = models.ForeignKey(Application, on_delete=models.CASCADE, verbose_name="Application")
    material = models.ForeignKey(Material, on_delete=models.PROTECT, verbose_name="Material")
    # bearings = models.CharField()
    spoke_holes = models.IntegerField(verbose_name="Number of spokes")
    rotor_mount = models.ForeignKey(RotorMountType, on_delete=models.PROTECT, verbose_name="Rotor mount type")
    freehub = models.ForeignKey(FreehubStandard, on_delete=models.PROTECT, verbose_name="Freehub Standard")
    # freehub_body_type = models.CharField()
    # gearing = models.CharField()
    axle_type = models.ForeignKey(AxleType, on_delete=models.PROTECT, verbose_name="Axle type")
    flange_distance = models.DecimalField(max_digits=3, decimal_places=1, verbose_name="Flange distance")
    partial_bolt_circle_diameter = models.DecimalField(max_digits=3, decimal_places=1,
                                                       verbose_name="Partial bolt_circle_diameter")
    # spoke_hole_diameter = models.CharField()
    features = models.TextField(verbose_name="Features", blank=True, null=True)
    technology = models.TextField(verbose_name="Technology", blank=True, null=True)
    color = models.CharField(max_length=50, verbose_name="Color")
    weight = models.DecimalField(max_digits=5, decimal_places=3, verbose_name="Weight (kg)", null=True, blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Price (€)", null=True, blank=True)
    image = models.ImageField(upload_to='components/hubs/', verbose_name="Rear hub Image", null=True, blank=True)

    def __str__(self):
        return f"{self.brand} {self.series} {self.freehub}/{self.axle_type}, Spokes - {self.spoke_holes}"


class WheelLacing(models.Model):
    lacing_type = models.CharField(max_length=50, verbose_name="Wheel lacing type")

    def __str__(self):
        return self.lacing_type


class FrontWheel(models.Model):
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE, verbose_name="Brand name")
    series = models.CharField(max_length=100, verbose_name="Series Name")
    application = models.ForeignKey(Application, on_delete=models.CASCADE, verbose_name="Application")
    wheel_size = models.ForeignKey(WheelSize, on_delete=models.PROTECT, verbose_name="Wheel size")
    # tyre_type = models.CharField()
    spokes_num = models.IntegerField(verbose_name="Number of spokes")
    rim = models.ForeignKey(Rim, on_delete=models.PROTECT, verbose_name="Rim")
    front_hub = models.ForeignKey(FrontHub, on_delete=models.PROTECT, verbose_name="Front hub")
    lacing = models.ForeignKey(WheelLacing, on_delete=models.PROTECT, verbose_name="Spokes lacing")
    rotor_mount = models.ForeignKey(RotorMountType, on_delete=models.PROTECT, verbose_name="Rotor mount type")
    tyre_width = models.BooleanField()
    tubeless_ready = models.BooleanField(verbose_name="Tubeless Ready")
    features = models.TextField(verbose_name="Features", blank=True, null=True)
    technology = models.TextField(verbose_name="Technology", blank=True, null=True)
    color = models.CharField(max_length=50, verbose_name="Color")
    weight = models.DecimalField(max_digits=5, decimal_places=3, verbose_name="Weight (kg)", null=True, blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Price (€)", null=True, blank=True)
    image = models.ImageField(upload_to='components/wheels/', verbose_name="Front wheel Image", null=True, blank=True)

    def __str__(self):
        return f"{self.brand} {self.series} / {self.wheel_size} (Spokes - {self.spokes_num}) TLR:{self.tubeless_ready}"


class RearWheel(models.Model):
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE, verbose_name="Brand name")
    series = models.CharField(max_length=100, verbose_name="Series Name")
    application = models.ForeignKey(Application, on_delete=models.CASCADE, verbose_name="Application")
    wheel_size = models.ForeignKey(WheelSize, on_delete=models.PROTECT, verbose_name="Wheel size")
    # tyre_type = models.CharField()
    spokes_num = models.IntegerField(verbose_name="Number of spokes")
    rim = models.ForeignKey(Rim, on_delete=models.PROTECT, verbose_name="Rim")
    rear_hub = models.ForeignKey(RearHub, on_delete=models.PROTECT, verbose_name="Rear hub")
    lacing = models.ForeignKey(WheelLacing, on_delete=models.PROTECT, verbose_name="Spokes lacing")
    rotor_mount = models.ForeignKey(RotorMountType, on_delete=models.PROTECT, verbose_name="Rotor mount type")
    tyre_width = models.BooleanField()
    tubeless_ready = models.BooleanField(verbose_name="Tubeless Ready")
    features = models.TextField(verbose_name="Features", blank=True, null=True)
    technology = models.TextField(verbose_name="Technology", blank=True, null=True)
    color = models.CharField(max_length=50, verbose_name="Color")
    weight = models.DecimalField(max_digits=5, decimal_places=3, verbose_name="Weight (kg)", null=True, blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Price (€)", null=True, blank=True)
    image = models.ImageField(upload_to='components/wheels/', verbose_name="Rear wheel Image", null=True, blank=True)

    def __str__(self):
        return f"{self.brand} {self.series} / {self.wheel_size} (Spokes - {self.spokes_num}) TLR:{self.tubeless_ready}"


class WheelSet(models.Model):
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE, verbose_name="Brand name")
    series = models.CharField(max_length=100, verbose_name="Series Name")
    application = models.ForeignKey(Application, on_delete=models.CASCADE, verbose_name="Application")
    wheel_size = models.ForeignKey(WheelSize, on_delete=models.PROTECT, verbose_name="Wheel size")
    # tyre_type = models.CharField()
    spokes_num = models.IntegerField(verbose_name="Number of spokes")
    rotor_mount = models.ForeignKey(RotorMountType, on_delete=models.PROTECT, verbose_name="Rotor mount type")
    tubeless_ready = models.BooleanField(verbose_name="Tubeless Ready")
    front_wheel = models.ForeignKey(FrontWheel, on_delete=models.PROTECT, verbose_name="Front wheel")
    rear_wheel = models.ForeignKey(RearWheel, on_delete=models.PROTECT, verbose_name="Rear wheel")
    weight_limit = models.IntegerField(verbose_name="Weight limit")

    # color = models.CharField(max_length=50, verbose_name="Color")
    features = models.TextField(verbose_name="Features", blank=True, null=True)
    technology = models.TextField(verbose_name="Technology", blank=True, null=True)
    weight = models.DecimalField(max_digits=5, decimal_places=3, verbose_name="Weight (kg)", null=True, blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Price (€)", null=True, blank=True)

    def __str__(self):
        return f"{self.brand} {self.series} / {self.wheel_size} TLR:{self.tubeless_ready}"

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

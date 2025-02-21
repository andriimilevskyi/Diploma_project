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
    diameter = models.IntegerField(max_length=2, verbose_name="Axle diameter")
    length = models.IntegerField(max_length=3, verbose_name="Axle length")
    side = models.CharField(max_length=15, verbose_name="Axle side")

    def __str__(self):
        return f"{self.side}/{self.type}, {self.diameter}mm/{self.length}mm"


class BBStandart(models.Model):
    name = models.CharField(max_length=15, verbose_name="Bottom Bracket standart name")
    type = models.CharField(max_length=15, verbose_name="Bottom Bracket standart type")

    def __str__(self):
        return f"{self.type}/{self.name}"


class FrontDerailleurMount(models.Model):
    name = models.CharField(max_length=15, verbose_name="Front Derailleur Mount standart name")
    type = models.CharField(max_length=15, verbose_name="Front Derailleur Mount standart type", null=True, blank=True)

    def __str__(self):
        return f"{self.name}, {self.type}"


class RotorDiameter(models.Model):
    diameter = models.IntegerField(max_length=3, verbose_name="Rotor diameter")

    def __str__(self):
        return f"{self.diameter}mm"


class RotorMountType(models.Model):
    type = models.CharField(max_length=50, verbose_name="Rottor Mount Type")

    def __str__(self):
        return self.type


class BrakeMountStandart(models.Model):
    name = models.CharField(max_length=15, verbose_name="Brake Mount standart name")
    rotor_size = models.ForeignKey(RotorDiameter, verbose_name="Rottor size in mm")

    def __str__(self):
        return f"{self.name} ({self.rotor_size}mm)"


class TubeDiameter(models.Model):
    diameter = models.DecimalField(max_digits=3, decimal_places=1)

    def __str__(self):
        return self.diameter


class Frame(models.Model):
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE)
    series = models.CharField(max_length=100, verbose_name="Series Name")
    application = models.ForeignKey(Application, verbose_name="Application")
    type = models.CharField(max_length=100, verbose_name="Type")
    wheel_size = models.ForeignKey(WheelSize, on_delete=models.CASCADE)
    tyre_size = models.ForeignKey(TyreSize, on_delete=models.CASCADE, verbose_name="Max Tyre size")
    axle_type = models.ForeignKey(AxleType, on_delete=models.CASCADE, verbose_name="Axle type")
    size = models.CharField(max_length=50, verbose_name="Size")
    seatpost = models.CharField(max_length=100, verbose_name="Seatpost")
    min_rider_height = models.DecimalField(max_digits=3, decimal_places=1, verbose_name="Minimal Rider Height (cm)",
                                           null=True,
                                           blank=True)
    max_rider_height = models.DecimalField(max_digits=3, decimal_places=1, verbose_name="Maximal Rider Height (cm)",
                                           null=True,
                                           blank=True)
    bb_standard = models.ForeignKey(BBStandart, verbose_name="Bottom Bracket Standard")
    fork_travel = models.IntegerField(max_length=3, verbose_name="Fork Travel")
    front_derailleur_mount = models.ForeignKey(FrontDerailleurMount, verbose_name="Front Derailleur Mount", null=True,
                                               blank=True)
    brake_mount = models.ForeignKey(BrakeMountStandart, verbose_name="Brake Mount")
    chainring_size_max = models.CharField(max_length=50, verbose_name="Max Chainring Size")
    features = models.TextField(verbose_name="Features", blank=True, null=True)
    technology = models.TextField(verbose_name="Technology", blank=True, null=True)
    color = models.CharField(max_length=50, verbose_name="Color")
    weight = models.DecimalField(max_digits=5, decimal_places=2, verbose_name="Weight (kg)", null=True, blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Price (€)", null=True, blank=True)

    def __str__(self):
        return f"{self.brand.name} {self.series} ({self.size}, {self.seatpost}) - {self.type}"


class Fork(models.Model):
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE)
    series = models.CharField(max_length=100, verbose_name="Series Name")
    application = models.ForeignKey(Application, verbose_name="Application")
    type = models.CharField()
    wheel_size = models.ForeignKey(WheelSize, on_delete=models.CASCADE)
    suspension_type = models.CharField()
    stem_diameter = models.ForeignKey(TubeDiameter, verbose_name="Steerer Tube Diameter (Stem)")
    travel = models.IntegerField(max_length=3, verbose_name="Fork Travel")
    offset = models.CharField()
    axle_type = models.ForeignKey(AxleType, on_delete=models.CASCADE, verbose_name="Axle type")
    brake_mount = models.ForeignKey(BrakeMountStandart, verbose_name="Brake Mount")
    remote = models.BooleanField()
    tyre_size = models.ForeignKey(TyreSize, on_delete=models.CASCADE, verbose_name="Max Tyre size")
    rotor_size_max = models.ForeignKey(RotorDiameter, verbose_name="Max Rotor size")
    features = models.TextField(verbose_name="Features", blank=True, null=True)
    technology = models.TextField(verbose_name="Technology", blank=True, null=True)
    color = models.CharField(max_length=50, verbose_name="Color")
    weight = models.DecimalField(max_digits=5, decimal_places=2, verbose_name="Weight (kg)", null=True, blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Price (€)", null=True, blank=True)

    def __str__(self):
        return f"{self.brand} {self.series} {self.wheel_size} {self.travel}mm/{self.suspension_type}"


class Handlebar(models.Model):
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE)
    series = models.CharField(max_length=100, verbose_name="Series Name")
    application = models.ForeignKey(Application, verbose_name="Application")
    width = models.IntegerField(verbose_name="Handlebar width")
    stem_clamp = models.ForeignKey(TubeDiameter, verbose_name="Stem (Handlebar) clamp size")
    rise = models.DecimalField()
    backsweep = models.DecimalField()
    upsweep = models.DecimalField()
    material = models.CharField()
    features = models.TextField(verbose_name="Features", blank=True, null=True)
    technology = models.TextField(verbose_name="Technology", blank=True, null=True)
    color = models.CharField(max_length=50, verbose_name="Color")
    weight = models.DecimalField(max_digits=5, decimal_places=2, verbose_name="Weight (kg)", null=True, blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Price (€)", null=True, blank=True)

    def __str__(self):
        return f"{self.brand} {self.series} {self.width}mm ({self.stem_clamp}mm"


class Stem(models.Model):
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE)
    series = models.CharField(max_length=100, verbose_name="Series Name")
    application = models.ForeignKey(Application, verbose_name="Application")
    steerer_clamp = models.ForeignKey(TubeDiameter, verbose_name="Steerer Tube Diameter (Stem)")
    handlebar_clamp = models.ForeignKey(TubeDiameter, verbose_name="Stem (Handlebar) clamp size")
    length = models.IntegerField()
    angle = models.CharField()
    stack_height = models.CharField()
    material = models.CharField()
    features = models.TextField(verbose_name="Features", blank=True, null=True)
    technology = models.TextField(verbose_name="Technology", blank=True, null=True)
    color = models.CharField(max_length=50, verbose_name="Color")
    weight = models.DecimalField(max_digits=5, decimal_places=2, verbose_name="Weight (kg)", null=True, blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Price (€)", null=True, blank=True)

    def __str__(self):
        return f"{self.brand} {self.series} {self.material} ({self.length}mm/{self.angle}°)"


class ChainringMountStandart(models.Model):
    type = models.CharField(max_length=100, verbose_name="Chainring mount standart type")

    def __str__(self):
        return self.type


class Crankset(models.Model):
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE)
    series = models.CharField(max_length=100, verbose_name="Series Name")
    application = models.ForeignKey(Application, verbose_name="Application")
    chainring_mount = models.ForeignKey(ChainringMountStandart, verbose_name="Chainring Mount Standart")
    gradation = models.CharField()
    crank_arm_length = models.DecimalField(max_digits=3, decimal_places=1, verbose_name="Crank Arm length")
    axle_diameter = models.CharField()
    chainline = models.CharField()
    bb = models.CharField()
    gearing = models.DecimalField()
    features = models.TextField(verbose_name="Features", blank=True, null=True)
    technology = models.TextField(verbose_name="Technology", blank=True, null=True)
    color = models.CharField(max_length=50, verbose_name="Color")
    weight = models.DecimalField(max_digits=5, decimal_places=2, verbose_name="Weight (kg)", null=True, blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Price (€)", null=True, blank=True)

    def __str__(self):
        return f"{self.brand} {self.series} {self.gearing} {self.gradation} {self.chainring_mount}"


class BottomBracket(models.Model):
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE)
    series = models.CharField(max_length=100, verbose_name="Series Name")
    application = models.ForeignKey(Application, verbose_name="Application")
    type = models.CharField()
    shell_width = models.CharField()
    axle_diameter = models.CharField()
    features = models.TextField(verbose_name="Features", blank=True, null=True)
    technology = models.TextField(verbose_name="Technology", blank=True, null=True)
    color = models.CharField(max_length=50, verbose_name="Color")
    weight = models.DecimalField(max_digits=5, decimal_places=2, verbose_name="Weight (kg)", null=True, blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Price (€)", null=True, blank=True)

    def __str__(self):
        return f"{self.brand} {self.series} {self.type}"


class Casette(models.Model):
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE)
    series = models.CharField(max_length=100, verbose_name="Series Name")
    gearing = models.DecimalField()
    gradation = models.CharField()
    gradation_all = models.CharField()
    smallest_gear = models.IntegerField(max_length=2, verbose_name="Smallest star")
    biggest_gear = models.IntegerField(max_length=2, verbose_name="Biggest star")
    material = models.CharField()
    application = models.ForeignKey(Application, verbose_name="Application")
    features = models.TextField(verbose_name="Features", blank=True, null=True)
    technology = models.TextField(verbose_name="Technology", blank=True, null=True)
    freehub_standart = models.CharField()
    color = models.CharField(max_length=50, verbose_name="Color")
    weight = models.DecimalField(max_digits=5, decimal_places=2, verbose_name="Weight (kg)", null=True, blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Price (€)", null=True, blank=True)

    def __str__(self):
        return f"{self.brand} {self.series} {self.gearing} ({self.gradation}, {self.freehub_standart})"


class Chain(models.Model):
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE)
    series = models.CharField(max_length=100, verbose_name="Series Name")
    links_num = models.IntegerField(max_length=3, verbose_name="Number of links")
    gearing = models.DecimalField()
    application = models.ForeignKey(Application, verbose_name="Application")
    clousing_type = models.CharField()
    directional = models.BooleanField()
    material = models.CharField()
    features = models.TextField(verbose_name="Features", blank=True, null=True)
    technology = models.TextField(verbose_name="Technology", blank=True, null=True)
    color = models.CharField(max_length=50, verbose_name="Color")
    weight = models.DecimalField(max_digits=5, decimal_places=2, verbose_name="Weight (kg)", null=True, blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Price (€)", null=True, blank=True)

    def __str__(self):
        return f"{self.brand} {self.series} {self.gearing}"


class Dirailleur(models.Model):
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE)
    series = models.CharField(max_length=100, verbose_name="Series Name")
    gearing = models.DecimalField()
    type = models.CharField()
    application = models.ForeignKey(Application, verbose_name="Application")
    smallest_gear = models.IntegerField(max_length=2, verbose_name="Smallest star compatible")
    biggest_gear = models.IntegerField(max_length=2, verbose_name="Biggest star compatible")
    material = models.CharField()
    features = models.TextField(verbose_name="Features", blank=True, null=True)
    technology = models.TextField(verbose_name="Technology", blank=True, null=True)
    color = models.CharField(max_length=50, verbose_name="Color")
    weight = models.DecimalField(max_digits=5, decimal_places=2, verbose_name="Weight (kg)", null=True, blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Price (€)", null=True, blank=True)

    def __str__(self):
        return f"{self.brand} {self.series} {self.gearing}"


class FrontDirailleur(models.Model):
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE)
    series = models.CharField(max_length=100, verbose_name="Series Name")
    gearing = models.DecimalField()
    type = models.CharField()
    application = models.ForeignKey(Application, verbose_name="Application")
    chainline = models.CharField()
    chainring_size_max = models.CharField(max_length=50, verbose_name="Max Chainring Size")
    capacity = models.CharField()
    material = models.CharField()
    features = models.TextField(verbose_name="Features", blank=True, null=True)
    technology = models.TextField(verbose_name="Technology", blank=True, null=True)
    mount = models.ForeignKey(FrontDerailleurMount, verbose_name="Front Derailleur Mount")
    color = models.CharField(max_length=50, verbose_name="Color")
    weight = models.DecimalField(max_digits=5, decimal_places=2, verbose_name="Weight (kg)", null=True, blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Price (€)", null=True, blank=True)

    def __str__(self):
        return f"{self.brand} {self.series} {self.gearing}"


class Shifter(models.Model):
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE)
    series = models.CharField(max_length=100, verbose_name="Series Name")
    gearing = models.DecimalField()
    type = models.CharField()
    application = models.ForeignKey(Application, verbose_name="Application")
    mount = models.CharField()
    material = models.CharField()
    features = models.TextField(verbose_name="Features", blank=True, null=True)
    technology = models.TextField(verbose_name="Technology", blank=True, null=True)
    color = models.CharField(max_length=50, verbose_name="Color")
    weight = models.DecimalField(max_digits=5, decimal_places=2, verbose_name="Weight (kg)", null=True, blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Price (€)", null=True, blank=True)

    def __str__(self):
        return f"{self.brand} {self.series} {self.gearing}"


class BrakePads(models.Model):
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE)
    series = models.CharField(max_length=100, verbose_name="Series Name")
    compound = models.CharField()
    plate_material = models.CharField()
    cooling_fins = models.CharField()
    features = models.TextField(verbose_name="Features", blank=True, null=True)
    technology = models.TextField(verbose_name="Technology", blank=True, null=True)
    weight = models.DecimalField(max_digits=5, decimal_places=2, verbose_name="Weight (kg)", null=True, blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Price (€)", null=True, blank=True)

    def __str__(self):
        return f"{self.brand} {self.series} {self.compound}"


class BrakeRotor(models.Model):
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE)
    series = models.CharField(max_length=100, verbose_name="Series Name")
    mount = models.CharField()
    diameter = models.ForeignKey(RotorDiameter, verbose_name="Rotor diameter")
    features = models.TextField(verbose_name="Features", blank=True, null=True)
    technology = models.TextField(verbose_name="Technology", blank=True, null=True)
    actuation = models.CharField(verbose_name="Brake pads material")
    # brake_pads = models.ForeignKey(Brake_Pads, verbose_name="Brake pads")
    color = models.CharField(max_length=50, verbose_name="Color")
    weight = models.DecimalField(max_digits=5, decimal_places=2, verbose_name="Weight (kg)", null=True, blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Price (€)", null=True, blank=True)

    def __str__(self):
        return f"{self.brand} {self.series} {self.diameter} ({self.mount})"


class BrakeLever(models.Model):
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE)
    series = models.CharField(max_length=100, verbose_name="Series Name")
    application = models.ForeignKey(Application, verbose_name="Application")
    type = models.CharField()
    actuation = models.CharField()
    mount = models.CharField()
    material = models.CharField()
    lever_length = models.CharField()
    lever_side = models.CharField(Name="Left or right")
    color = models.CharField(max_length=50, verbose_name="Color")
    features = models.TextField(verbose_name="Features", blank=True, null=True)
    technology = models.TextField(verbose_name="Technology", blank=True, null=True)
    weight = models.DecimalField(max_digits=5, decimal_places=2, verbose_name="Weight (kg)", null=True, blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Price (€)", null=True, blank=True)

    def __str__(self):
        return f"{self.brand} {self.series} {self.type} {self.color}/{self.lever_side}"


class BrakeCaliper(models.Model):
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE)
    series = models.CharField(max_length=100, verbose_name="Series Name")
    application = models.ForeignKey(Application, verbose_name="Application")
    type = models.CharField()
    actuation = models.CharField()
    mount = models.CharField()
    mounting_position = models.CharField()
    caliper_material = models.CharField()
    piston_material = models.CharField()
    hose_connection = models.CharField()
    brake_pads = models.ForeignKey(BrakePads, verbose_name="Brake pads")
    rotor_compatibility = models.CharField()
    color = models.CharField(max_length=50, verbose_name="Color")
    features = models.TextField(verbose_name="Features", blank=True, null=True)
    technology = models.TextField(verbose_name="Technology", blank=True, null=True)
    weight = models.DecimalField(max_digits=5, decimal_places=2, verbose_name="Weight (kg)", null=True, blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Price (€)", null=True, blank=True)

    def __str__(self):
        return f"{self.brand} {self.series} {self.type} {self.color}/{self.mounting_position}"


class Brakes(models.Model):
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE)
    series = models.CharField(max_length=100, verbose_name="Series Name")
    application = models.ForeignKey(Application, verbose_name="Application")
    type = models.CharField()
    actuation = models.CharField()
    front_hose_length = models.IntegerField()
    caliper = models.ForeignKey(BrakeCaliper, verbose_name="Brake caliper")
    lever = models.ForeignKey(BrakeLever, verbose_name="Brake lever")
    brake_pads = models.ForeignKey(BrakePads, verbose_name="Brake pads")
    features = models.TextField(verbose_name="Features", blank=True, null=True)
    technology = models.TextField(verbose_name="Technology", blank=True, null=True)
    color = models.CharField(max_length=50, verbose_name="Color")
    weight = models.DecimalField(max_digits=5, decimal_places=2, verbose_name="Weight (kg)", null=True, blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Price (€)", null=True, blank=True)

    def __str__(self):
        return f"{self.brand} {self.series} {self.type}"


class DiskBrakeAdapter(models.Model):
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE)
    series = models.CharField(max_length=100, verbose_name="Series Name")
    type = models.CharField()
    material = models.CharField()
    rotor_size = models.CharField()
    mount = models.CharField()
    caliper_mount = models.CharField()
    color = models.CharField(max_length=50, verbose_name="Color")
    weight = models.DecimalField(max_digits=5, decimal_places=2, verbose_name="Weight (kg)", null=True, blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Price (€)", null=True, blank=True)

    def __str__(self):
        return f"{self.brand} {self.series} ({self.mount} to {self.caliper_mount})"


class Rim(models.Model):
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE)
    series = models.CharField(max_length=100, verbose_name="Series Name")
    wheel_size = models.ForeignKey(WheelSize, verbose_name="Wheel size")
    spokes_num = models.IntegerField(max_length="2", verbose_name="Number of spokes")
    tyre_type = models.CharField()
    features = models.TextField(verbose_name="Features", blank=True, null=True)
    technology = models.TextField(verbose_name="Technology", blank=True, null=True)
    weight = models.DecimalField(max_digits=5, decimal_places=2, verbose_name="Weight (kg)", null=True, blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Price (€)", null=True, blank=True)
    # add rims brakes
    def __str__(self):
        return f"{self.brand} {self.series} {self.wheel_size}/{self.spokes_num}"


class FrontHub(models.Model):
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE)
    series = models.CharField(max_length=100, verbose_name="Series Name")
    application = models.ForeignKey(Application, verbose_name="Application")
    material = models.CharField()
    bearings = models.CharField()
    spoke_holes = models.IntegerField(max_length=2, verbose_name="Number of spokes")
    rotor_mount = models.ForeignKey(RotorMountType, verbose_name="Rotor mount type")
    axle_type = models.ForeignKey(AxleType, verbose_name="Axle type")
    flange_distance = models.DecimalField(max_digits=3, decimal_places=1, verbose_name="Flange distance")
    partial_bolt_circle_diameter = models.DecimalField(max_digits=3, decimal_places=1,
                                                       verbose_name="Partial bolt_circle_diameter")
    spoke_hole_diameter = models.CharField()
    features = models.TextField(verbose_name="Features", blank=True, null=True)
    technology = models.TextField(verbose_name="Technology", blank=True, null=True)
    color = models.CharField(max_length=50, verbose_name="Color")
    weight = models.DecimalField(max_digits=5, decimal_places=2, verbose_name="Weight (kg)", null=True, blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Price (€)", null=True, blank=True)

    def __str__(self):
        return f"{self.brand} {self.series} {self.axle_type}, Spokes - {self.spoke_holes}"


class RearHub(models.Model):
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE)
    series = models.CharField(max_length=100, verbose_name="Series Name")
    application = models.ForeignKey(Application, verbose_name="Application")
    material = models.CharField()
    bearings = models.CharField()
    spoke_holes = models.IntegerField(max_length=2, verbose_name="Number of spokes")
    rotor_mount = models.ForeignKey(RotorMountType, verbose_name="Rotor mount type")
    freehub = models.CharField()
    freehub_body_type = models.CharField()
    gearing = models.CharField()
    axle_type = models.ForeignKey(AxleType, verbose_name="Axle type")
    flange_distance = models.DecimalField(max_digits=3, decimal_places=1, verbose_name="Flange distance")
    partial_bolt_circle_diameter = models.DecimalField(max_digits=3, decimal_places=1,
                                                       verbose_name="Partial bolt_circle_diameter")
    spoke_hole_diameter = models.CharField()
    features = models.TextField(verbose_name="Features", blank=True, null=True)
    technology = models.TextField(verbose_name="Technology", blank=True, null=True)
    color = models.CharField(max_length=50, verbose_name="Color")
    weight = models.DecimalField(max_digits=5, decimal_places=2, verbose_name="Weight (kg)", null=True, blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Price (€)", null=True, blank=True)

    def __str__(self):
        return f"{self.brand} {self.series} {self.freehub}/{self.axle_type}, Spokes - {self.spoke_holes}"


class FrontWheel(models.Model):
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE)
    series = models.CharField(max_length=100, verbose_name="Series Name")
    application = models.ForeignKey(Application, verbose_name="Application")
    wheel_size = models.ForeignKey(WheelSize, verbose_name="Wheel size")
    tyre_type = models.CharField()
    spokes_num = models.IntegerField(max_length="2", verbose_name="Number of spokes")
    rim = models.ForeignKey(Rim, verbose_name="Rim")
    front_hub = models.ForeignKey(FrontHub, verbose_name="Front hub")
    lacing = models.CharField()
    rotor_mount = models.ForeignKey(RotorMountType, verbose_name="Rotor mount type")
    tyre_width = models.BooleanField()
    tubeless_ready = models.BooleanField(verbose_name="Tubeless Ready")
    features = models.TextField(verbose_name="Features", blank=True, null=True)
    technology = models.TextField(verbose_name="Technology", blank=True, null=True)
    color = models.CharField(max_length=50, verbose_name="Color")
    weight = models.DecimalField(max_digits=5, decimal_places=2, verbose_name="Weight (kg)", null=True, blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Price (€)", null=True, blank=True)

    def __str__(self):
        return f"{self.brand} {self.series} / {self.wheel_size} (Spokes - {self.spokes_num}) TLR:{self.tubeless_ready}"


class RearWheel(models.Model):
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE)
    series = models.CharField(max_length=100, verbose_name="Series Name")
    application = models.ForeignKey(Application, verbose_name="Application")
    wheel_size = models.ForeignKey(WheelSize, verbose_name="Wheel size")
    tyre_type = models.CharField()
    spokes_num = models.IntegerField(max_length="2", verbose_name="Number of spokes")
    rim = models.ForeignKey(Rim, verbose_name="Rim")
    rear_hub = models.ForeignKey(RearHub, verbose_name="Rear hub")
    lacing = models.CharField()
    rotor_mount = models.ForeignKey(RotorMountType, verbose_name="Rotor mount type")
    tyre_width = models.BooleanField()
    tubeless_ready = models.BooleanField(verbose_name="Tubeless Ready")
    features = models.TextField(verbose_name="Features", blank=True, null=True)
    technology = models.TextField(verbose_name="Technology", blank=True, null=True)
    color = models.CharField(max_length=50, verbose_name="Color")
    weight = models.DecimalField(max_digits=5, decimal_places=2, verbose_name="Weight (kg)", null=True, blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Price (€)", null=True, blank=True)

    def __str__(self):
        return f"{self.brand} {self.series} / {self.wheel_size} (Spokes - {self.spokes_num}) TLR:{self.tubeless_ready}"


class Wheelset(models.Model):
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE)
    series = models.CharField(max_length=100, verbose_name="Series Name")
    application = models.ForeignKey(Application, verbose_name="Application")
    wheel_size = models.ForeignKey(WheelSize, verbose_name="Wheel size")
    tyre_type = models.CharField()
    spokes_num = models.IntegerField(max_length="2", verbose_name="Number of spokes")
    rotor_mount = models.ForeignKey(RotorMountType, verbose_name="Rotor mount type")
    tubeless_ready = models.BooleanField(verbose_name="Tubeless Ready")
    front_wheel = models.ForeignKey(FrontWheel, verbose_name="Front wheel")
    rear_wheel = models.ForeignKey(RearWheel, verbose_name="Rear wheel")
    weight_limit = models.IntegerField(max_length=3, verbose_name="Weight limit")

    # color = models.CharField(max_length=50, verbose_name="Color")
    features = models.TextField(verbose_name="Features", blank=True, null=True)
    technology = models.TextField(verbose_name="Technology", blank=True, null=True)
    weight = models.DecimalField(max_digits=5, decimal_places=2, verbose_name="Weight (kg)", null=True, blank=True)
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

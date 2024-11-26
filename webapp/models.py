from django.db import models

# Create your models here.


class Case(models.Model):
    name = models.CharField(max_length=100, verbose_name="Case Name")
    type = models.CharField(max_length=50, choices=[
        ('A14', 'iPhone 14'),
        ('A14 Plus', 'iPhone 14 Plus'),
        ('A14 Pro', 'iPhone 14 Pro'),
        ('A14 Pro Max', 'iPhone 14 Pro Max'),
        ('ASE2', 'iPhone SE 2'),
        ('ASE3', 'iPhone SE 3'),
        ('A15', 'iPhone 15'),
        ('A15 Plus', 'iPhone 15 Plus'),
        ('A15 Pro', 'iPhone 15 Pro'),
        ('A15 Pro Max', 'iPhone 15 Pro Max'),
        ('A16', 'iPhone 16'),
        ('A16 Plus', 'iPhone 16 Plus'),
        ('A16 Pro', 'iPhone 16 Pro Max'),
        ('A16 Pro Max', 'iPhone 16 Pro Max'),
    ], verbose_name="Type")
    color = models.CharField(max_length=50, verbose_name="Color")
    material = models.CharField(max_length=50, verbose_name="Material")
    features = models.TextField(verbose_name="Features")
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Price")
    s_description = models.CharField(max_length=150, verbose_name="Short Description")
    description = models.TextField(verbose_name="Full Description")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.name} ({self.type})"


class Order(models.Model):
    first_name = models.CharField(max_length=50, verbose_name="First Name")
    last_name = models.CharField(max_length=50, verbose_name="Last Name")
    email = models.EmailField(verbose_name="Email Address")
    phone = models.CharField(max_length=20, verbose_name="Phone Number")
    datetime = models.DateTimeField(auto_now_add=True, verbose_name="Order Date")

    def __str__(self):
        return f"Order №{self.id} by {self.first_name} {self.last_name}"

    @property
    def total_price(self):
        return sum(item.total_price for item in self.items.all())


class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name="items")
    case = models.ForeignKey(Case, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)

    def __str__(self):
        return f"{self.quantity} x {self.case.name}"

    @property
    def total_price(self):
        return self.quantity * self.case.price

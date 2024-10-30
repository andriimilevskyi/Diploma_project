from django.db import models

# Create your models here.
from django.db import models


class Case(models.Model):
    name = models.CharField(max_length=100)
    type = models.CharField()
    color = models.CharField(max_length=50)
    material = models.CharField(max_length=50)
    features = models.CharField(max_length=50)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    s_description = models.CharField()
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class Order(models.Model):
    first_name = models.CharField()
    second_name = models.CharField()
    email = models.CharField()
    phone = models.CharField()
    case_id = models.ManyToManyRel(Case)
    datatime = models.DateTimeField(auto_now=True)

    def __str__(self):
        return (self.id, self.case_id, self.phone, self.email)

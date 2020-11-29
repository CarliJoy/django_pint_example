from django.db import models
from quantityfield import UnitRegistry
from quantityfield.fields import IntegerQuantityField, QuantityField


class Box(models.Model):
    name = models.TextField()
    height = IntegerQuantityField
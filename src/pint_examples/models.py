from django.db import models

from quantityfield.fields import IntegerQuantityField, QuantityField


class Box(models.Model):
    name = models.TextField()
    height = IntegerQuantityField("millimeter")
    width = QuantityField("beer")
    length = QuantityField("meter")

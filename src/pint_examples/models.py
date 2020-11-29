from django.db import models

from quantityfield.fields import IntegerQuantityField, QuantityField


class Box(models.Model):
    name = models.TextField()
    height = IntegerQuantityField("millimeter", blank=True, default=10)
    width = QuantityField("finger", unit_choices=["millimeter", "meter"])
    length = QuantityField("meter")

    volume = QuantityField("liter", null=True, blank=True)

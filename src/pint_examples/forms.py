from django.forms import ModelForm

from quantityfield.fields import QuantityFormField

from pint_examples.models import Box


class BoxModelForm(ModelForm):
    new_weight = QuantityFormField(
        base_units="gram", unit_choices=["gram", "ounce", "milligram"]
    )

    class Meta:
        model = Box
        exclude = []

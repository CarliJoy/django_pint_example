from django.forms import Form, ModelForm

from quantityfield.fields import QuantityFormField

from pint_examples.models import Box


class BoxModelForm(ModelForm):
    new_weight = QuantityFormField(
        base_units="gram", unit_choices=["gram", "ounce", "milligram"]
    )

    class Meta:
        model = Box
        exclude = []


class SimpleForm(Form):
    hello = QuantityFormField(base_units="kilogram", required=False)

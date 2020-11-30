# Create your views here.
from django.shortcuts import render
from django.views.generic import FormView

from pint_examples.forms import SimpleForm


class SimpleForm(FormView):
    template_name = "pint_examples/form_base.html"
    form_class = SimpleForm
    success_url = "/success"


def success(request):
    return render(request, "pint_examples/success.html")

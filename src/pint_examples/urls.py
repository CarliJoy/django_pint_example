from django.urls import path

from pint_examples.views import SimpleForm, success

urlpatterns = [path("simple/", SimpleForm.as_view()), path("success", success)]

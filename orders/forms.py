from django import forms
from .models import Order
from localflavor.us.forms import USZipCodeField
from django.utils.translation import gettext_lazy as _


class OrderCreateForm(forms.ModelForm):
    postal_code = USZipCodeField(label=_('Postal code'))

    class Meta:
        model = Order
        fields = ['first_name', 'last_name', 'email', 'address', 'postal_code', 'city']

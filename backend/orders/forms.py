from django import forms
from localflavor.pl.forms import PLPostalCodeField
from .models import Order


class OrderCreateForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        prefix = kwargs.pop('prefix', '')
        super().__init__(*args, **kwargs)

        if prefix == 'pl':
            self.fields['postal_code'] = PLPostalCodeField()

    class Meta:
        model = Order
        fields = ['first_name', 'last_name', 'email', 'address', 'postal_code', 'city']

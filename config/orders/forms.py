from django import forms
from .models import Order

class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ["full_name", "phone", "email", "people"]

        widgets = {
            "full_name": forms.TextInput(attrs={
                "placeholder": "Your full name"
            }),
            "phone": forms.TextInput(attrs={
                "placeholder": "+996 XXX XXX XXX"
            }),
            "email": forms.EmailInput(attrs={
                "placeholder": "Email (optional)"
            }),
            "people": forms.NumberInput(attrs={
                "min": 1
            }),
        }

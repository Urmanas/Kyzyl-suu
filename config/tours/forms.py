from django import forms 
from .models import Tour


class TourForm(forms.ModelForm):
    class Meta:
        model = Tour
        fields = '__all__'
        widgets = {
            'title': forms.TextInput(attrs={'class': 'w-full border px-4 py-2 rounded'}),
            'description': forms.Textarea(attrs={'class': 'w-full border px-4 py-2 rounded'}),
            'price': forms.NumberInput(attrs={'class': 'w-full border px-4 py-2 rounded'}),
        }
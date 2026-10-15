from .models import ONG
from django import forms

class OngForm(forms.ModelForm):
    class Meta:
        model = ONG
        fields = '__all__'
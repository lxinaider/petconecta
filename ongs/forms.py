from django import forms

from .models import Ong


class OngForm(forms.ModelForm):
    class Meta:
        model = Ong
        fields = '__all__'
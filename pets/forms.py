from django import forms

from .models import Pet


class PetForm(forms.ModelForm):
    class Meta:
        model = Pet
        fields = ["name", "species", "breed", "image", "description"]  # noqa: RUF012

        labels = {  # noqa: RUF012
            "name": "Nome",
            "species": "Espécie",
            "breed": "Raça",
            "image": "Imagem",
            "description": "Descrição",
        }

        widgets = {  # noqa: RUF012
            "name": forms.TextInput(attrs={"class": "form-control"}),
            "species": forms.TextInput(attrs={"class": "form-control"}),
            "breed": forms.TextInput(
                attrs={
                    "class": "form-control",
                }
            ),
            "image": forms.FileInput(attrs={"class": "form-control"}),
            "description": forms.Textarea(
                attrs={
                    "class": "form-control",
                    "rows": 4,
                }
            ),
        }

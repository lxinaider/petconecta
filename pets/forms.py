from django import forms

from .models import AdopterProfile, AdoptionRequest, Pet


class AdopterProfileForm(forms.ModelForm):
    class Meta:
        model = AdopterProfile
        exclude = ["user"]
        labels = {
            "birth_date": "Data de nascimento",
            "cpf": "CPF",
            "zip_code": "CEP",
            "address": "Endereço",
            "city": "Cidade",
            "state": "UF",
            "housing": "Tipo de moradia",
            "is_rented": "A moradia é alugada",
            "allows_pets": "O proprietário permite animais",
            "has_protection": "Tenho telas nas janelas ou muros",
            "household_size": "Pessoas na casa",
            "has_children": "Há crianças na casa",
            "other_pets": "Outros animais (quais e quantos)",
            "experience": "Experiência com animais",
        }
        widgets = {
            "birth_date": forms.DateInput(attrs={"type": "date"}, format="%Y-%m-%d"),
            "other_pets": forms.Textarea(attrs={"rows": 3}),
            "experience": forms.Textarea(attrs={"rows": 3}),
        }


class AdoptionRequestForm(forms.ModelForm):
    household_agrees = forms.BooleanField(
        label="Todos que moram comigo concordam com a adoção", required=True
    )
    accept_terms = forms.BooleanField(
        label="Concordo com o termo de adoção responsável",
        required=True,
    )

    class Meta:
        model = AdoptionRequest
        fields = ["motivation", "hours_alone", "household_agrees"]
        labels = {
            "motivation": "Por que você quer adotar este animal?",
            "hours_alone": "Quantas horas por dia ele ficaria sozinho?",
        }
        widgets = {"motivation": forms.Textarea(attrs={"rows": 4})}


class PetForm(forms.ModelForm):
    class Meta:
        model = Pet
        fields = ["name", "species", "breed", "image", "description"]

        labels = {
            "name": "Nome",
            "species": "Espécie",
            "breed": "Raça",
            "image": "Imagem",
            "description": "Descrição",
        }

        widgets = {
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

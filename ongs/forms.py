from django import forms

from .models import Ong


class OngForm(forms.ModelForm):
    class Meta:
        model = Ong
        fields = [  # noqa: RUF012
            "legal_name",
            "trade_name",
            "cnpj",
            "email",
            "phone",
            "city",
            "state",
            "description",
        ]

        labels = {  # noqa: RUF012
            "legal_name": "Nome legal",
            "trade_name": "Nome fantasia",
            "cnpj": "CNPJ",
            "email": "E-mail",
            "phone": "Telefone",
            "state": "UF",
            "city": "Cidade",
            "description": "Descrição",
        }

        widgets = {  # noqa: RUF012
            "legal_name": forms.TextInput(attrs={"class": "form-control"}),
            "trade_name": forms.TextInput(attrs={"class": "form-control"}),
            "cnpj": forms.TextInput(
                attrs={
                    "class": "form-control",
                    "placeholder": "Somente números",
                }
            ),
            "email": forms.EmailInput(attrs={"class": "form-control"}),
            "phone": forms.TextInput(attrs={"class": "form-control"}),
            "city": forms.TextInput(attrs={"class": "form-control"}),
            "state": forms.TextInput(
                attrs={
                    "class": "form-control",
                    "maxlength": 2,
                    "placeholder": "Ex.: MT",
                }
            ),
            "description": forms.Textarea(
                attrs={
                    "class": "form-control",
                    "rows": 4,
                }
            ),
        }

from django import forms
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm

from .models import User


class RegisterForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = User
        fields = ("name", "email", "phone")

        labels = {  # noqa: RUF012
            "name": "Nome completo",
            "email": "E-mail",
            "phone": "Telefone",
        }

        widgets = {  # noqa: RUF012
            "name": forms.TextInput(attrs={"class": "form-control"}),
            "email": forms.EmailInput(attrs={"class": "form-control"}),
            "phone": forms.TextInput(attrs={"class": "form-control"}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields["password1"].widget.attrs.update({"class": "form-control"})
        self.fields["password2"].widget.attrs.update({"class": "form-control"})


class LoginForm(AuthenticationForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields["username"].label = "E-mail"
        self.fields["username"].widget = forms.EmailInput(
            attrs={
                "class": "form-control",
                "placeholder": "Digite seu e-mail",
                "autocomplete": "email",
            }
        )
        self.fields["password"].label = "Password"
        self.fields["password"].widget.attrs.update(
            {
                "class": "form-control",
                "placeholder": "Digite sua senha",
            }
        )

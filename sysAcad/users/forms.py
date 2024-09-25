from django import forms
from django.core.exceptions import ValidationError
from django.contrib.auth.models import User
from django.contrib.auth import get_user_model

User = get_user_model()

class StudentProfessorForm(forms.Form):
    ROLE_CHOICES = [
        ("professor", "Professor"),
        ("student", "Estudante"),
    ]

    role = forms.ChoiceField(label="Tipo", choices=ROLE_CHOICES, widget=forms.RadioSelect)
    name = forms.CharField(label="Nome completo", max_length=64)
    email = forms.EmailField(label="Email", max_length=32)
    cellphone = forms.CharField(label="Celular", max_length=14)
    password = forms.CharField(label="Senha", widget=forms.PasswordInput)
    password_confirm = forms.CharField(label="Confirmar Senha", widget=forms.PasswordInput)

    birth_date = forms.DateField(
        label="Data de nascimento",
        widget=forms.DateInput(
            attrs={
                "type": "date"
            }
        )
    )

    def clean_email(self):
        email = self.cleaned_data.get('email')
        if User.objects.filter(email=email).exists():
            raise ValidationError("Este email já está em uso. Tente outro.")
        return email

    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get("password")
        password_confirm = cleaned_data.get("password_confirm")

        if password != password_confirm:
            raise forms.ValidationError("Passwords do not match")

        return cleaned_data


class LoginForm(forms.Form):
    ROLE_CHOICES = [
        ("professor", "Professor"),
        ("student", "Estudante"),
    ]

    role = forms.ChoiceField(label="Tipo", choices=ROLE_CHOICES, widget=forms.RadioSelect)
    email = forms.EmailField(label="Email", max_length=32)
    password = forms.CharField(label="Senha", widget=forms.PasswordInput)


class EditInfoForm(forms.Form):
    name = forms.CharField(
        label="Nome completo",
        max_length=64,
        required=False
    )
    email = forms.EmailField(
        label="Email",
        max_length=32,
        required=False
    )
    cellphone = forms.CharField(
        label="Celular",
        max_length=14,
        required=False
    )
    password = forms.CharField(
        label="Senha",
        widget=forms.PasswordInput,
        required=False
    )
    password_confirm = forms.CharField(
        label="Confirmar Senha",
        widget=forms.PasswordInput,
        required=True
    )
    birth_date = forms.DateField(
        label="Data de nascimento",
        widget=forms.DateInput(
            attrs={
                "type": "date"
            }
        ),
        required=False
    )

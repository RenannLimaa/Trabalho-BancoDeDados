from django import forms
from course.models import Course


class StudentProfessorForm(forms.Form):
    ROLE_CHOICES = [
        ("professor", "Professor"),
        ("student", "Estudante"),
    ]

    role = forms.ChoiceField(
        choices=ROLE_CHOICES,
        widget=forms.RadioSelect(attrs={'class': 'role-radio'})  # Optional for styling
    )

    name = forms.CharField(
        max_length=64,
        widget=forms.TextInput(attrs={
            'placeholder': 'Digite seu nome completo'
        })
    )

    email = forms.EmailField(
        max_length=32,
        widget=forms.EmailInput(attrs={
            'placeholder': 'Digite seu e-mail'
        })
    )

    cellphone = forms.CharField(
        max_length=14,
        widget=forms.TextInput(attrs={
            'placeholder': 'Digite seu celular'
        })
    )

    password = forms.CharField(
        widget=forms.PasswordInput(attrs={
            'placeholder': 'Digite sua senha'
        })
    )

    password_confirm = forms.CharField(
        widget=forms.PasswordInput(attrs={
            'placeholder': 'Confirme sua senha'
        })
    )

    course = forms.ModelChoiceField(
        queryset=Course.objects.all(),
        required=True,
        label="Curso",
        widget=forms.Select()
    )

    birth_date = forms.DateField(
        label="Data de nascimento",
        widget=forms.DateInput(attrs={
            'type': 'date',
        })
    )

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

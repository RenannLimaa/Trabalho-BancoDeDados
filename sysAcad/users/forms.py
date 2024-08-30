from django import forms


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

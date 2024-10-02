from django import forms
from django.core.exceptions import ValidationError
from django.contrib.auth import get_user_model
from course.models import Course

User = get_user_model()

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

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # If role is provided in POST data
        role = self.data.get("role")
        if role == "professor":
            self.fields["course"].required = False  # Make course not required for professors
            self.fields["course"].widget.attrs['disabled'] = 'disabled'  # Disable the course field

    def clean_email(self):
        email = self.cleaned_data.get('email')
        if User.objects.filter(email=email).exists():
            raise ValidationError("Este email já está em uso. Tente outro.")
        return email

    def clean(self):
        cleaned_data = super().clean()
        role = cleaned_data.get("role")
        course = cleaned_data.get("course")
        password = cleaned_data.get("password")
        password_confirm = cleaned_data.get("password_confirm")

        # Check if passwords match
        if password and password_confirm and password != password_confirm:
            raise forms.ValidationError("Passwords do not match")

        # Handle 'course' field based on the selected role
        if role == "professor":
            # Make course optional for professors
            self.fields['course'].required = False
            cleaned_data['course'] = None  # Set course to None for professors
        else:
            # For students, ensure the course is selected
            if not course:
                self.add_error('course', "Selecione um curso.")

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
        required=False
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

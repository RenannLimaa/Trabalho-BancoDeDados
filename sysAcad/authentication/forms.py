from django import forms


class StudentProfessorForm(forms.Form):
    ROLE_CHOICES = [
        ("professor", "Professor"),
        ("estudante", "Estudante"),
    ]

    role = forms.ChoiceField(label="Tipo", choices=ROLE_CHOICES, widget=forms.RadioSelect)
    name = forms.CharField(label="Nome completo", max_length=64)
    email = forms.EmailField(label="Email", max_length=32)
    cellphone = forms.CharField(label="Celular", max_length=14)

    birth_date = forms.DateField(
        label="Data de nascimento",
        widget=forms.DateInput(
            attrs={
                "type": "date"
            }
        )
    )

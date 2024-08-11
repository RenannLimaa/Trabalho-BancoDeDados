from django.contrib import messages
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, render
from django.urls import reverse
from users.forms import EditInfoForm

from .models import Professor


@login_required
def home(request):
    professor = Professor.objects.get(user=request.user)
    return render(request, "professor/home.html", {"professor": professor})


def remove_professor(request):
    if request.method == "POST":
        try:
            professor = Professor.objects.get(user=request.user)
            user = professor.user
            user.delete()
            messages.success(request, "Conta excluída com sucesso")
            return redirect("login")
        except Professor.DoesNotExist:
            messages.error(request, "Erro ao excluir a conta")
            return redirect(reverse("professor_home"))


def edit_professor(request):
    try:
        professor = Professor.objects.get(user=request.user)

    except Professor.DoesNotExist:
        messages.error(request, "Professor não encontrado")
        return redirect(reverse("professor_home"))

    if request.method == "POST":
        form = EditInfoForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data.get("name")
            email = form.cleaned_data.get("email")
            cellphone = form.cleaned_data.get("cellphone")
            password = form.cleaned_data.get("password")
            birth_date = form.cleaned_data.get("birth_date")

            professor.name = name
            professor.email = email
            professor.cellphone = cellphone
            professor.password = password
            professor.birth_date = birth_date

            user = professor.user
            user.username = email
            if password:
                user.set_password(password)
            user.save()
            professor.save()
            login(request, user)

            messages.success(request, "Informações atualizadas com sucesso.")
            return redirect(reverse("professor_home"))

        else:
            messages.error(request, "Erro ao atualizar informações")

    else:
        form = EditInfoForm(
            initial={
                "name": professor.name,
                "email": professor.email,
                "cellphone": professor.cellphone,
                "birth_date": professor.birth_date,
            }
        )
    return render(request, "professor/edit_info.html", {"form": form})

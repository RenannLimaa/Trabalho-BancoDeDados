from django.contrib import messages
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, render
from django.urls import reverse
from users.forms import EditInfoForm

from .models import Student

# Create your views here.


@login_required
def home(request):
    student = Student.objects.get(user=request.user)
    return render(request, "student/home.html", {"student": student})


def remove_student(request):
    if request.method == "POST":
        try:
            student = Student.objects.get(user=request.user)
            user = student.user
            user.delete()
            messages.success(request, "Conta excluída com sucesso")
            return redirect("login")
        except Student.DoesNotExist:
            messages.error(request, "Erro ao excluir a conta")
            return redirect(reverse("student_home"))

    else:
        messages.error(request, "else: Erro ao excluir a conta")
        return redirect(reverse("student_home"))


def edit_student(request):
    try:
        student = Student.objects.get(user=request.user)

    except Student.DoesNotExist:
        messages.error(request, "Estudante não encontrado")
        return redirect(reverse("student_home"))

    if request.method == "POST":
        form = EditInfoForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data.get("name")
            email = form.cleaned_data.get("email")
            cellphone = form.cleaned_data.get("cellphone")
            password = form.cleaned_data.get("password")
            birth_date = form.cleaned_data.get("birth_date")

            student.name = name
            student.email = email
            student.cellphone = cellphone
            student.password = password
            student.birth_date = birth_date

            user = student.user
            user.username = email
            if password:
                user.set_password(password)
            user.save()
            student.save()
            login(request, user)

            messages.success(request, "Informações atualizadas com sucesso.")
            return redirect(reverse("student_home"))

        else:
            messages.error(request, "Erro ao atualizar informações")

    else:
        form = EditInfoForm(
            initial={
                "name": student.name,
                "email": student.email,
                "cellphone": student.cellphone,
                "birth_date": student.birth_date,
            }
        )
    return render(request, "student/edit_info.html", {"form": form})

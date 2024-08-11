from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, render
from django.urls import reverse
from users.models import User

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
        except User.DoesNotExist:
            messages.error(request, "Erro ao excluir a conta")
            return redirect(reverse("student_home"))

    else:
        messages.error(request, "else: Erro ao excluir a conta")
        return redirect(reverse("student_home"))


def edit_student(request):
    pass

from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.hashers import make_password
from .forms import StudentProfessorForm
from student.models import Student
from professor.models import Professor


def signup(request):
    if request.method == 'POST':
        form = StudentProfessorForm(request.POST)
        if form.is_valid():
            role = form.cleaned_data['role']
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            cellphone = form.cleaned_data['cellphone']
            birth_date = form.cleaned_data['birth_date']
            password = form.cleaned_data['password']

            hashed_password = make_password(password)

            if role == "professor":
                professor = Professor.objects.create(
                    name=name,
                    email=email,
                    cellphone=cellphone,
                    birth_date=birth_date,
                    password=hashed_password
                )

                professor.save()

            elif role == "student":
                student = Student.objects.create(
                    name=name,
                    email=email,
                    cellphone=cellphone,
                    birth_date=birth_date,
                    password=hashed_password
                )

                student.save()

        return render(request, "authentication/signup.html", {'form': form})
    else:
        form = StudentProfessorForm()

    return render(request, "authentication/signup.html", {'form': form})

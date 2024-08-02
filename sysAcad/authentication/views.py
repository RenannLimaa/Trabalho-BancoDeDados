from django.shortcuts import render, redirect
from users.forms import StudentProfessorForm, LoginForm
from student.models import Student
from professor.models import Professor
from users.models import User
from django.contrib.auth import authenticate, login
from django.urls import reverse


def user_register(request):
    if request.method == 'POST':
        form = StudentProfessorForm(request.POST)
        if form.is_valid():
            role = form.cleaned_data.get('role')
            name = form.cleaned_data.get('name')
            email = form.cleaned_data.get('email')
            cellphone = form.cleaned_data.get('cellphone')
            password = form.cleaned_data.get('password')
            birth_date = form.cleaned_data.get('birth_date')

            if role == 'student':
                user = User.objects.create_user(username=email, email=email, password=password, is_student=True, is_professor=False)
                student = Student.objects.create(user=user, name=name, email=email, cellphone=cellphone, birth_date=birth_date)
                student.save()

            elif role == 'professor':
                user = User.objects.create_user(username=email, email=email, password=password, is_student=False, is_professor=True)
                professor = Professor.objects.create(user=user, name=name, email=email, cellphone=cellphone, birth_date=birth_date)
                professor.save()

            return redirect(reverse("login"))
    else:
        form = StudentProfessorForm()

    return render(request, "authentication/signup.html", {'form': form})


def user_login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            role = form.cleaned_data.get('role')
            email = form.cleaned_data.get('email')
            password = form.cleaned_data.get('password')

            user = authenticate(request, username=email, password=password)
            if user is not None and ((role == 'student' and user.is_student) or (role == 'professor' and user.is_professor)):
                login(request, user)
                return redirect(reverse('home'))
            else:
                form.add_error(None, "Invalid credentials or role")
    else:
        form = LoginForm()

    return render(request, 'authentication/login.html', {'form': form})

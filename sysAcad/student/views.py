from django.contrib import messages
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse
from users.forms import EditInfoForm
from .models import Student
from classes.models import Classes
from grade.models import Grade
from subject.models import Subject
from django.db.models import Q


# Create your views here.
@login_required
def student_home(request):
    if request.method == "POST":
        return redirect(reverse("logout"))
    student = get_object_or_404(Student, user=request.user)
    return render(request, "student/home.html", {"student": student})
    


@login_required
def remove_student(request):
    if request.method == "POST":
        try:
            student = get_object_or_404(Student, user=request.user)
            user = student.user
            user.delete()
            messages.success(request, "Conta excluída com sucesso.")
            return redirect("login")
        except Student.DoesNotExist:
            messages.error(request, "Erro ao excluir a conta.")
            return redirect("student_home")


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

            messages.success(request, "Informações atualizadas com sucesso!")
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
    return render(request, "student/edit_info.html", {"form": form, "student": student})


@login_required 
def enroll_in_classes(request):  
    student = Student.objects.get(user=request.user)

    if request.method == "POST":
        if request.user.is_authenticated:
            try:
                selected_classes = request.POST.getlist("classes")

                if student.get_number_of_enrolled_classes() > 7:
                    messages.error(request, "Não é possível se matricular em mais de 7 disciplinas")
                    return redirect("class_enrollment")

                if not selected_classes:
                    messages.error(request, "Nenhuma turma selecionada")
                    return redirect("class_enrollment")

                for class_id in selected_classes:
                    class_instance = Classes.objects.get(id=class_id)

                    if student.is_enrolled_in_class(class_instance):
                        messages.error(request, "Aluno não pode se matricular em mais de uma turma da mesma disciplina")
                        return redirect("class_enrollment")

                    student.classes.add(class_instance)

                messages.success(request, "Turmas matriculadas com sucesso!")
                return redirect("class_enrollment")

            except Student.DoesNotExist:
                messages.error(request, "Estudante não encontrado")
                return redirect("login")

            except Classes.DoesNotExist:
                messages.error(request, "Uma ou mais turmas não existem")
                return redirect("class_enrollment")


    classes = Classes.objects.filter(subject__course=student.course)
    classes = classes.exclude(
    Q(subject__notas__student=student) &
    Q(subject__notas__status='Aprovado')
    ).distinct()

    return render(request, "student/class_enrollment.html", {"classes": classes, "student": student})


@login_required
def remove_classes(request):
    student = Student.objects.get(user=request.user)

    if request.method == "POST":
        if request.user.is_authenticated:
            try:
                selected_classes = request.POST.getlist("classes")

                if not selected_classes:
                    messages.error(request, "Nenhuma disciplina selecionada")
                    return redirect("remove_classes")

                for class_id in selected_classes:
                    classes = Classes.objects.get(id=class_id)
                    student.classes.remove(classes)

                messages.success(request, "Turmas removidas com sucesso!")
                return redirect("remove_classes")

            except Student.DoesNotExist:
                messages.error(request, "Estudante não encontrado")
                return redirect("login")

            except Classes.DoesNotExist:
                messages.error(request, "Uma ou mais turmas não existe")
                return redirect("remove_classes")

    classes = student.classes.all()
    return render(request, "student/remove_classes.html", {"classes": classes, "student": student})

@login_required
def student_history(request):
    student = request.user.student  
    
    # Filtra as notas do estudante
    grades = Grade.objects.filter(student=student).select_related('subject')

    # Prepara os dados para o template
    grades_data = []
    for grade in grades:
        avg = grade.calculate_average()  
        status = grade.status  
        grades_data.append({
            'subject_name': grade.subject.name,
            'grade1': grade.grade1,
            'grade2': grade.grade2,
            'grade3': grade.grade3,
            'average': avg,
            'status': status  
        })

    context = {
        'grades_data': grades_data, 'student': student
    }

    return render(request, 'student/student_history.html', context)

@login_required
def view_curriculum(request):
    # Recupera o estudante associado ao usuário logado
    student = get_object_or_404(Student, user=request.user)
    
    # Recupera o curso do estudante
    course = student.course
    
    # Recupera todas as disciplinas associadas ao curso
    subjects = Subject.objects.filter(course=course)
    
    # Renderiza a página com as disciplinas
    return render(request, 'student/view_subjects.html', {
        'student': student,
        'course': course,
        'subjects': subjects,
    })

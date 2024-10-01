from django.contrib import messages
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse
from users.forms import EditInfoForm
from classes.models import Classes
from grade.models import Grade
from .models import Professor


def get_logged_in_professor(request):
    try:
        return Professor.objects.get(user=request.user)
    except Professor.DoesNotExist:
        return None

@login_required
def home(request):
    professor = get_logged_in_professor(request)
    if not professor:
        return redirect('login')  # Redireciona se o professor não for encontrado
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

@login_required
def register_in_class(request):
    professor = get_logged_in_professor(request)
    try:
        # Obter o professor logado
        professor = Professor.objects.get(user=request.user)
        
        if request.method == "POST":
            class_id = request.POST.get('class_id')
            class_instance = Classes.objects.get(id=class_id)


            # Verificar se o professor já está atribuído a outra turma
            if class_instance.professor:
                messages.error(request, "Esta turma já tem um professor atribuído.")
            else:
                # Atribuir o professor à turma
                class_instance.professor = professor
                class_instance.save()
                messages.success(request, f"Você foi cadastrado na turma {class_instance} com sucesso.")
                return redirect('register_in_class')  # Redirecionar após o cadastro

        # Obter todas as turmas disponíveis
        available_classes = Classes.objects.filter(professor__isnull=True)
        
        return render(request, 'professor/register_in_class.html', {
            'available_classes': available_classes,
            'professor': professor
            })
    
    except Professor.DoesNotExist:
        messages.error(request, "Professor não encontrado.")
        return redirect('login')

@login_required
def view_current_classes(request):
    professor = get_logged_in_professor(request)  # Usa a função para obter o professor logado
    if not professor:
        return redirect('login')  # Redireciona se o professor não for encontrado

    # Obter todas as turmas atribuídas ao professor logado
    current_classes = Classes.objects.filter(professor=professor)

    return render(request, 'professor/current_classes.html', {
        'professor': professor,  
        'current_classes': current_classes
    })



@login_required
def view_students_in_class(request, class_id):
    professor = get_logged_in_professor(request)
    class_instance = get_object_or_404(Classes, id=class_id)

    if class_instance.professor.user != request.user:
        messages.error(request, "Você não tem permissão para ver os estudantes dessa turma.")
        return redirect('view_current_classes')

    students = class_instance.students.all()
    grades_by_student = {
        grade.student.user.id: grade  
        for grade in Grade.objects.filter(student__in=students, subject=class_instance.subject)
    }

    if request.method == 'POST':
        for student in students:
            grade1 = request.POST.get(f'grade1_{student.user.id}')
            grade2 = request.POST.get(f'grade2_{student.user.id}')
            grade3 = request.POST.get(f'grade3_{student.user.id}')

            # Obter ou criar o objeto de Grade correspondente
            grade, created = Grade.objects.get_or_create(student=student, subject=class_instance.subject)

            # Atualizar as notas se elas forem válidas
            if grade1 is not None:
                try:
                    grade.grade1 = float(grade1) if grade1 else None
                except ValueError:
                    messages.error(request, f"Nota 1 inválida para o aluno {student.name}")
                    return redirect('view_students_in_class', class_id=class_id)

            if grade2 is not None:
                try:
                    grade.grade2 = float(grade2) if grade2 else None
                except ValueError:
                    messages.error(request, f"Nota 2 inválida para o aluno {student.name}")
                    return redirect('view_students_in_class', class_id=class_id)

            if grade3 is not None:
                try:
                    grade.grade3 = float(grade3) if grade3 else None
                except ValueError:
                    messages.error(request, f"Nota 3 inválida para o aluno {student.name}")
                    continue

            grade.save()  # Salva o objeto Grade após atualizar as notas

        messages.success(request, "Notas atualizadas com sucesso.")
        return redirect('view_students_in_class', class_id=class_id)

    return render(request, 'professor/students_in_class.html', {
        'class_instance': class_instance,
        'students': students,
        'grades_by_student': grades_by_student,
        'professor': professor
    })

@login_required
def complete_class(request, class_id):
    class_instance = get_object_or_404(Classes, id=class_id)

    if class_instance.professor.user != request.user:
        messages.error(request, "Você não tem permissão para concluir esta turma.")
        return redirect('view_current_classes')

    if request.method == 'POST':
        if class_instance.all_grades_assigned():
            class_instance.is_completed = True
            class_instance.save()
            messages.success(request, "Turma concluída com sucesso.")
            return redirect('view_current_classes')
        else:
            messages.error(request, "Não é possível concluir a turma. Certifique-se de que todas as notas foram atribuídas.")

    return render(request, 'professor/complete_class.html', {
        'class_instance': class_instance
    })

@login_required
def view_completed_classes(request):
    completed_classes = Classes.objects.filter(professor__user=request.user, is_completed=True)  # Filtra turmas concluídas
    return render(request, 'professor/completed_classes.html', {'completed_classes': completed_classes})

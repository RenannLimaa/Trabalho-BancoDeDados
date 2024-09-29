from django.db import models
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _
from grade.models import Grade
from django.utils import timezone

class Day(models.Model):
    DAYS_OF_WEEK = [
        ('Monday', 'Segunda-feira'),
        ('Tuesday', 'Terça-feira'),
        ('Wednesday', 'Quarta-feira'),
        ('Thursday', 'Quinta-feira'),
        ('Friday', 'Sexta-feira'),
        ('Saturday', 'Sábado'),
        ('Sunday', 'Domingo'),
    ]

    name = models.CharField(max_length=9, choices=DAYS_OF_WEEK, unique=True)

    def __str__(self):
        return self.name


class Classes(models.Model):
    id = models.AutoField(primary_key=True)
    classroom = models.CharField(max_length=32)
    vacancies = models.PositiveIntegerField()

    start_time = models.TimeField()
    end_time = models.TimeField()
    days_of_week = models.ManyToManyField(Day, related_name="classes")

    subject = models.ForeignKey("subject.Subject", on_delete=models.CASCADE, related_name="classes")
    professor = models.ForeignKey("professor.Professor", on_delete=models.CASCADE, related_name="classes")

    is_completed = models.BooleanField(default=False)
    date_completed = models.DateTimeField(null=True, blank=True)

    def clean(self):
        if self.start_time >= self.end_time:
            raise ValidationError(_('O horário de início deve ser antes do horário de término.'))

    class Meta:
        verbose_name = "Class"
        verbose_name_plural = "Classes"
    
    def clean(self):
        # Verificar se o horário de início é antes do término
        if self.start_time >= self.end_time:
            raise ValidationError(_('O horário de início deve ser antes do horário de término.'))

        # Procurar por conflitos de horário para turmas não concluídas
        conflicting_classes = Classes.objects.filter(
            classroom=self.classroom,
            start_time__lt=self.end_time,
            end_time__gt=self.start_time,
            is_completed=False  # Apenas turmas não concluídas
        ).exclude(id=self.id)  # Exclui a própria turma, caso esteja sendo editada

        if conflicting_classes.exists():
            raise ValidationError(_('Já existe uma turma não concluída com conflito de horário nesta sala de aula.'))
            
    def all_grades_assigned(self):
        # Verifica se todos os alunos têm notas atribuídas
        students = self.students.all()
        for student in students:
            grades = Grade.objects.filter(student=student, subject=self.subject)
            if not grades.exists() or any(g.grade1 is None or g.grade2 is None or g.grade3 is None for g in grades):
                return False
        return True
    
    def save(self, *args, **kwargs):
        if self.is_completed and not self.date_completed:
            self.date_completed = timezone.now()  # Define a data de conclusão ao salvar
        super().save(*args, **kwargs)


    def __str__(self):
        return f"{self.subject} - {self.professor}"

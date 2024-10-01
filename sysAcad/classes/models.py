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

    def clean(self):
        if self.start_time >= self.end_time:
            raise ValidationError(_('O horário de início deve ser antes do horário de término.'))

    class Meta:
        verbose_name = "Class"
        verbose_name_plural = "Classes"
    
    def all_grades_assigned(self):
        students = self.students.all()
        for student in students:
            grades = Grade.objects.filter(student=student, subject=self.subject)
            if not grades.exists() or any(g.grade1 is None or g.grade2 is None or g.grade3 is None for g in grades):
                return False
        return True


    def __str__(self):
        return f"{self.subject} - {self.professor}"

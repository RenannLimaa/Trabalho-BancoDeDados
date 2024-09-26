from django.db import models
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _

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

        for day in self.days_of_week.all():
            conflicting_classes = Classes.objects.filter(
                classroom=self.classroom,
                days_of_week=day,
                start_time__lt=self.end_time,  # Conflicting class starts before this one ends
                end_time__gt=self.start_time    # Conflicting class ends after this one starts
            ).exclude(id=self.id)


        if conflicting_subjects.exists():
            raise ValidationError(_('Já existe uma turma com conflito de horário nesta sala de aula.'))

    class Meta:
        verbose_name = "Class"
        verbose_name_plural = "Classes"


    def __str__(self):
        return f"{self.subject} - {self.professor}"

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


    

    class Meta:
        verbose_name = "Class"
        verbose_name_plural = "Classes"


    def __str__(self):
        return f"{self.subject} - {self.professor}"

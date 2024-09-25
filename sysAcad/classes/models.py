from django.db import models
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _

class Classes(models.Model):
    DAYS_OF_WEEK = [
        ('Monday', 'Monday'),
        ('Tuesday', 'Tuesday'),
        ('Wednesday', 'Wednesday'),
        ('Thursday', 'Thursday'),
        ('Friday', 'Friday'),
        ('Saturday', 'Saturday'),
        ('Sunday', 'Sunday'),
    ]

    id = models.AutoField(primary_key=True)
    classroom = models.CharField(max_length=32)
    start_time = models.TimeField()
    day_of_week = models.CharField(max_length=10, choices=DAYS_OF_WEEK)
    end_time = models.TimeField()
    subject = models.ForeignKey("subject.Subject", on_delete=models.CASCADE, related_name="classes")
    professor = models.ForeignKey("professor.Professor", on_delete=models.CASCADE, related_name="classes")

    def clean(self):
        # Verificar se o horário de início é antes do término
        if self.start_time >= self.end_time:
            raise ValidationError(_('O horário de início deve ser antes do horário de término.'))

        # Procurar por conflitos de horário
        conflicting_subjects = Classes.objects.filter(
            classroom=self.classroom,
            day_of_week=self.day_of_week,
            start_time__lt=self.end_time,  # Início de outra aula antes do término desta
            end_time__gt=self.start_time    # Término de outra aula depois do início desta
        ).exclude(id=self.id)

        if conflicting_subjects.exists():
            raise ValidationError(_('Já existe uma turma com conflito de horário nesta sala de aula.'))

    def __str__(self):
        return self.classroom

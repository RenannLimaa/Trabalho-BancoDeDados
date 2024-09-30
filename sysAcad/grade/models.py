from django.db import models


class Grade(models.Model):
    id = models.AutoField(primary_key=True)
    student = models.ForeignKey("student.Student", related_name='notas', on_delete=models.CASCADE)
    subject = models.ForeignKey("subject.Subject", related_name='notas', on_delete=models.CASCADE)
    grade1 = models.FloatField(null=True, blank=True)
    grade2 = models.FloatField(null=True, blank=True)
    grade3 = models.FloatField(null=True, blank=True)

    def calculate_average(self):
        grades = [g for g in [self.grade1, self.grade2, self.grade3] if g is not None]
        return sum(grades) / len(grades) if grades else None

    def __str__(self):
        return f"Nota para {self.aluno.nome} em {self.disciplina.nome}: {self.nota}"

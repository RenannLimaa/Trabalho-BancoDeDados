from django.db import models


class Grade(models.Model):
    id = models.AutoField(primary_key=True)
    grade = models.DecimalField(max_digits=5, decimal_places=2)
    student = models.ForeignKey("student.Student", related_name='notas', on_delete=models.CASCADE)
    subject = models.ForeignKey("subject.Subject", related_name='notas', on_delete=models.CASCADE)

    def __str__(self):
        return f"Nota para {self.aluno.nome} em {self.disciplina.nome}: {self.nota}"

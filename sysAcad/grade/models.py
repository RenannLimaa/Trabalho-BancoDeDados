from django.db import models
from course.models import Disciplina, Curso
from student.models import Student
from professor.models import Professor

# Create your models here.
class Nota(models.Model):
    id = models.AutoField(primary_key=True)
    nota = models.DecimalField(max_digits=5, decimal_places=2)
    aluno = models.ForeignKey(Student, related_name='notas', on_delete=models.CASCADE)
    disciplina = models.ForeignKey(Disciplina, related_name='notas', on_delete=models.CASCADE)

    def __str__(self):
        return f"Nota para {self.aluno.nome} em {self.disciplina.nome}: {self.nota}"

class Matricula(models.Model):
    aluno = models.ForeignKey(Student, related_name='matriculas', on_delete=models.CASCADE)
    curso = models.ForeignKey(Curso, related_name='matriculas', on_delete=models.CASCADE)
    disciplina = models.ForeignKey(Disciplina, related_name='matriculas', on_delete=models.CASCADE)

    class Meta:
        unique_together = ('aluno', 'curso', 'disciplina')

    def __str__(self):
        return f"{self.aluno.nome} - {self.curso.nome} - {self.disciplina.nome}"

class Turma(models.Model):
    id = models.AutoField(primary_key=True)
    sala = models.CharField(max_length=50)
    horario = models.CharField(max_length=100)
    disciplina = models.ForeignKey(Disciplina, related_name='turmas', on_delete=models.CASCADE)
    professor = models.ForeignKey(Professor, related_name='turmas', on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.disciplina.nome} - {self.sala}"
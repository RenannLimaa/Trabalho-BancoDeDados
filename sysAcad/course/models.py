from django.db import models

# Create your models here.
class Curso(models.Model):
    idcurso = models.AutoField(primary_key=True)
    nome = models.CharField(max_length=255)
    duracao = models.CharField(max_length=100)  

    def __str__(self):
        return self.nome
    
class Disciplina(models.Model):
    idDisciplina = models.AutoField(primary_key=True)
    nome = models.CharField(max_length=255)
    quantidadeVagas = models.PositiveIntegerField()

    def __str__(self):
        return self.nome
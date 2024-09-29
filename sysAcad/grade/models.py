from django.db import models


class Grade(models.Model):
    id = models.AutoField(primary_key=True)
    student = models.ForeignKey("student.Student", related_name='notas', on_delete=models.CASCADE)
    subject = models.ForeignKey("subject.Subject", related_name='notas', on_delete=models.CASCADE)
    grade1 = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True)
    grade2 = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True)
    grade3 = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True)
    status = models.CharField(max_length=10, blank=True, null=True)
    
    def calculate_average(self):
            grades = [self.grade1, self.grade2, self.grade3]
            valid_grades = [grade for grade in grades if grade is not None]  # Filtra as notas válidas
            if valid_grades:
                return sum(valid_grades) / len(valid_grades)
            return None  # Retorna None se não houver notas válidas
    
    def save(self, *args, **kwargs):
        average = self.calculate_average()
        if average is not None:
            self.status = "Aprovado" if average >= 7 else "Reprovado"
        else:
            self.status = "Sem notas suficientes"
        super().save(*args, **kwargs)

    def __str__(self):
        return f"Nota para {self.student.name} em {self.subject.name}: {self.calculate_average()}"

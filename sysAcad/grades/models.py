from django.db import models

from students.models import Student
from subjects.models import Subject


class Grade(models.Model):
    student = models.ForeignKey(
        Student, related_name="grades", on_delete=models.CASCADE
    )
    subject = models.ForeignKey(
        Subject, related_name="grades", on_delete=models.CASCADE
    )
    grade1 = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True)
    grade2 = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True)
    grade3 = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True)

    def __str__(self):
        return f"{self.student.name} - {self.subject.name}: {self.grade1}, {self.grade2}, {self.grade3}"

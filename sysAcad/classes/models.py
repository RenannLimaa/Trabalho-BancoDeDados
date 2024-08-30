from django.db import models

from students.models import Student
from subjects.models import Subject


class Class(models.Model):
    subject = models.ForeignKey(
        Subject, related_name="classes", on_delete=models.CASCADE
    )
    students = models.ManyToManyField(Student, related_name="classes")
    room = models.CharField(max_length=32)
    schedule = models.CharField(max_length=15)  # 24AB
    seat_count = models.IntegerField()

    def __str__(self):
        return f"{self.subject.name} - {self.schedule} - Sala: {self.room}"

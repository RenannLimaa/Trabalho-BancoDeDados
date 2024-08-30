from django.db import models

from courses.models import Course
from professors.models import Professor


class Subject(models.Model):
    name = models.CharField(max_length=128)
    description = models.TextField()
    course = models.ForeignKey(
        Course, related_name="subjects", on_delete=models.CASCADE
    )
    professors = models.ManyToManyField(Professor, related_name="subjects")

    def __str__(self):
        return self.name

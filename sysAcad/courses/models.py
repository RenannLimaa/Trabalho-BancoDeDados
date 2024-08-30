from django.db import models

from professors.models import Professor


class Course(models.Model):
    name = models.CharField(max_length=128)
    description = models.TextField()
    professors = models.ManyToManyField(Professor, related_name="courses")

    def __str__(self):
        return self.name

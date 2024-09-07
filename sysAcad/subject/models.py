from django.db import models


class Subject(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    vacancies = models.PositiveIntegerField()
    course = models.ForeignKey("course.Course", on_delete=models.CASCADE, related_name="subjects")

    def __str__(self):
        return self.nome

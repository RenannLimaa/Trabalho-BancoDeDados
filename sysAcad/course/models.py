from django.db import models


class Course(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=128)
    duration = models.CharField(max_length=32)

    def __str__(self):
        return self.name

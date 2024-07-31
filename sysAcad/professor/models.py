from django.db import models

# Create your models here.


class Professor(models.Model):
    name = models.CharField(max_length=64)
    email = models.CharField(max_length=32)
    cellphone = models.CharField(max_length=14)
    birth_date = models.DateField(auto_now=False, auto_now_add=False)
    registration = models.CharField(max_length=8, primary_key=True)

    def __str__(self):
        return self.name

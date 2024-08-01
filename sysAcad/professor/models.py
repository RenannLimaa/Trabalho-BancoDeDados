from django.db import models

# Create your models here.


class Professor(models.Model):
    name = models.CharField(max_length=64)
    email = models.CharField(max_length=32)
    cellphone = models.CharField(max_length=14)
    birth_date = models.DateField(auto_now=False, auto_now_add=False)
    registration = models.BigAutoField(primary_key=True)
    password = models.CharField(max_length=128)

    def __str__(self):
        return self.name

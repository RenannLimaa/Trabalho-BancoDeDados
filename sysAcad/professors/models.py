from django.db import models


class Professor(models.Model):

    email = models.EmailField()
    name = models.CharField(max_length=64)
    cellphone = models.CharField(max_length=14)
    birth_date = models.DateField(auto_now=False, auto_now_add=False)

    def __str__(self):
        return self.name

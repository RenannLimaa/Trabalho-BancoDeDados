from django.db import models
from django.conf import settings
from datetime import date

class Professor(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, primary_key=True)
    email = models.EmailField()
    name = models.CharField(max_length=64)
    cellphone = models.CharField(max_length=14)
    birth_date = models.DateField(auto_now=False, auto_now_add=False)

    def get_age(self):
        today = date.today()
        age = today.year - self.birth_date.year - ((today.month, today.day) < (self.birth_date.month, self.birth_date.day))
        return age

    def __str__(self):
        return self.name
    
    def get_first_name(self):
        names = self.name.split()
        return names[0]

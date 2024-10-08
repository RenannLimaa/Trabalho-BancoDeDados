from datetime import date
from django.conf import settings
from django.db import models


class Student(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, primary_key=True)
    email = models.EmailField()
    name = models.CharField(max_length=64)
    cellphone = models.CharField(max_length=14)
    birth_date = models.DateField(auto_now=False, auto_now_add=False)
    course = models.ForeignKey("course.Course", related_name="students", on_delete=models.CASCADE)
    classes = models.ManyToManyField("classes.Classes", related_name="students")

    def get_first_name(self):
        names = self.name.split()
        return names[0]

    def get_age(self):
        today = date.today()
        age = (today.year - self.birth_date.year - ((today.month, today.day) < (self.birth_date.month, self.birth_date.day)))
        return age

    def is_enrolled_in_class(self, class_obj):
        return self.classes.filter(subject=class_obj.subject).exists()

    def get_number_of_enrolled_classes(self):
        return self.classes.count()


    def __str__(self):
        return self.name

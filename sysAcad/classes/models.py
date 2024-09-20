from django.db import models


class Day(models.Model):
    DAYS_OF_WEEK = [
        ('Monday', 'Monday'),
        ('Tuesday', 'Tuesday'),
        ('Wednesday', 'Wednesday'),
        ('Thursday', 'Thursday'),
        ('Friday', 'Friday'),
        ('Saturday', 'Saturday'),
        ('Sunday', 'Sunday'),
    ]

    name = models.CharField(max_length=9, choices=DAYS_OF_WEEK, unique=True)

    def __str__(self):
        return self.name


class Classes(models.Model):
    id = models.AutoField(primary_key=True)
    classroom = models.CharField(max_length=32)
    vacancies = models.PositiveIntegerField()

    start_time = models.TimeField()
    end_time = models.TimeField()
    days_of_week = models.ManyToManyField(Day, related_name="classes")

    subject = models.ForeignKey("subject.Subject", on_delete=models.CASCADE, related_name="classes")
    professor = models.ForeignKey("professor.Professor", on_delete=models.CASCADE, related_name="classes")

    class Meta:
        verbose_name = "Class"
        verbose_name_plural = "Classes"

    def __str__(self):
        return self.classroom

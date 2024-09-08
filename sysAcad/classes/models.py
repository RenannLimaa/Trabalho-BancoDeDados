from django.db import models


class Classes(models.Model):
    DAYS_OF_WEEK = [
        ('Monday', 'Monday'),
        ('Tuesday', 'Tuesday'),
        ('Wednesday', 'Wednesday'),
        ('Thursday', 'Thursday'),
        ('Friday', 'Friday'),
        ('Saturday', 'Saturday'),
        ('Sunday', 'Sunday'),
    ]

    id = models.AutoField(primary_key=True)
    classroom = models.CharField(max_length=32)
    start_time = models.TimeField()
    day_of_week = models.CharField(max_length=10, choices=DAYS_OF_WEEK)
    end_time = models.TimeField()
    subject = models.ForeignKey("subject.Subject", on_delete=models.CASCADE, related_name="classes")
    professor = models.ForeignKey("professor.Professor", on_delete=models.CASCADE, related_name="classes")

    class Meta:
        verbose_name = "Class"
        verbose_name_plural = "Classes"

    def __str__(self):
        return self.classroom

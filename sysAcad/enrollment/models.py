from django.db import models
from student.models import Student
from course.models import Course
from subject.models import Subject


class Enrollment(models.Model):
    student = models.ForeignKey(Student, related_name='matriculas', on_delete=models.CASCADE)
    course = models.ForeignKey(Course, related_name='matriculas', on_delete=models.CASCADE)
    subject = models.ForeignKey(Subject, related_name='matriculas', on_delete=models.CASCADE)
    
    

    class Meta:
        unique_together = ("student", "course", "subject")

    def __str__(self):
        return f"{self.student.name} - {self.course.name} - {self.subject.name}"

from rest_framework.serializers import ModelSerializer

from students.serializers import StudentSerializer
from subjects.serializers import SubjectSerializer

from .models import Grade


class GradeSerializer(ModelSerializer):
    student = StudentSerializer(read_only=True)
    subject = SubjectSerializer(read_only=True)

    class Meta:
        model = Grade
        fields = ["id", "student", "subject", "grade1", "grade2", "grade3"]

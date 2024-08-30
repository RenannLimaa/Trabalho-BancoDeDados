from rest_framework.serializers import ModelSerializer

from students.serializers import StudentSerializer
from subjects.serializers import SubjectSerializer

from .models import Class


class ClassSerializer(ModelSerializer):
    subject = SubjectSerializer(read_only=True)
    students = StudentSerializer(many=True, read_only=True)

    class Meta:
        model = Class
        fields = ["id", "subject", "room", "schedule", "seat_count", "students"]

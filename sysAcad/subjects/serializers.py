from rest_framework.serializers import ModelSerializer

from courses.serializers import CourseSerializer
from professors.serializers import ProfessorSerializer

from .models import Subject


class SubjectSerializer(ModelSerializer):
    course = CourseSerializer(read_only=True)
    professors = ProfessorSerializer(many=True, read_only=True)

    class Meta:
        model = Subject
        fields = ["id", "name", "description", "course", "professors"]

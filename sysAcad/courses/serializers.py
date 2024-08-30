from rest_framework.serializers import ModelSerializer

from professors.serializers import ProfessorSerializer

from .models import Course


class CourseSerializer(ModelSerializer):
    professors = ProfessorSerializer(many=True, read_only=True)

    class Meta:
        model = Course
        fields = ["id", "name", "description", "professors"]

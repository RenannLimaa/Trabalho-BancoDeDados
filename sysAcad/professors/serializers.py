from rest_framework.serializers import ModelSerializer

from .models import Professor


class ProfessorSerializer(ModelSerializer):
    class Meta:
        model = Professor
        fields = ["name", "email", "cellphone"]

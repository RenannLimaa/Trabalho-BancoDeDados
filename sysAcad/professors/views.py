from django.views.generic import G
from rest_framework.viewsets import GenericViewSet

from .filters import ProfessorFilter
from .models import Professor
from .serializers import ProfessorSerializer


class ProfessorViewSet(GenericViewSet):
    queryset = Professor.objects.all().order_by("-id")
    serializer_class = ProfessorSerializer
    filterset_class = ProfessorFilter

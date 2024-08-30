from django.views.generic import G
from rest_framework.viewsets import GenericViewSet

from .filters import GradeFilter
from .models import Grade
from .serializers import GradeSerializer


class ClassViewSet(GenericViewSet):
    queryset = Grade.objects.all().order_by("-id")
    serializer_class = GradeSerializer
    filterset_class = GradeFilter

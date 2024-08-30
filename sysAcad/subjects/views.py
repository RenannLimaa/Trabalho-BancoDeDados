from django.views.generic import G
from rest_framework.viewsets import GenericViewSet

from .filters import SubjectFilter
from .models import Subject
from .serializers import SubjectSerializer


class SubjectViewSet(GenericViewSet):
    queryset = Subject.objects.all().order_by("-id")
    serializer_class = SubjectSerializer
    filterset_class = SubjectFilter

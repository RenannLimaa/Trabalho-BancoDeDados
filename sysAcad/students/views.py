from django.views.generic import G
from rest_framework.viewsets import GenericViewSet

from .filters import StudentFilter
from .models import Student
from .serializers import StudentSerializer


class StudentViewSet(GenericViewSet):
    queryset = Student.objects.all().order_by("-id")
    serializer_class = StudentSerializer
    filterset_class = StudentFilter

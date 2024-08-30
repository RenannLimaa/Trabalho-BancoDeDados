from rest_framework.viewsets import GenericViewSet

from .filters import CourseFilter
from .models import Course
from .serializers import CourseSerializer


class CourseViewSet(GenericViewSet):
    queryset = Course.objects.all().order_by("-id")
    serializer_class = CourseSerializer
    filterset_class = CourseFilter

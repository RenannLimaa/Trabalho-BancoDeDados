from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView

from .filters import CourseFilter
from .models import Course
from .serializers import CourseSerializer


class CourseList(ListCreateAPIView):
    serializer_class = CourseSerializer
    queryset = Course.objects.all()

    def perform_create(self, serializer):
        serializer.save()

    def get_queryset(self):
        return self.queryset.all()


class CourseDetailAPIView(RetrieveUpdateDestroyAPIView):
    serializer_class = CourseSerializer
    queryset = Course.objects.all()
    lookup_field = "id"

    def get_queryset(self):
        return self.queryset.all()

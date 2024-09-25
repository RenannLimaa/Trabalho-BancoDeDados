from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView

from .filters import StudentFilter
from .models import Student
from .serializers import StudentSerializer


class StudentList(ListCreateAPIView):
    serializer_class = StudentSerializer
    queryset = Student.objects.all()

    def perform_create(self, serializer):
        serializer.save()

    def get_queryset(self):
        return self.queryset.all()


class StudentDetailAPIView(RetrieveUpdateDestroyAPIView):
    serializer_class = StudentSerializer
    queryset = Student.objects.all()
    lookup_field = "id"

    def get_queryset(self):
        return self.queryset.all()

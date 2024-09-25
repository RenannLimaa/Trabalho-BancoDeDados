from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView

from .filters import ClassFilter
from .models import Class
from .serializers import ClassSerializer


class ClassList(ListCreateAPIView):
    serializer_class = ClassSerializer
    queryset = Class.objects.all()

    def perform_create(self, serializer):
        serializer.save()

    def get_queryset(self):
        return self.queryset.all()


class ClassDetailAPIView(RetrieveUpdateDestroyAPIView):
    serializer_class = ClassSerializer
    queryset = Class.objects.all()
    lookup_field = "id"

    def get_queryset(self):
        return self.queryset.all()

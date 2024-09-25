from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView

from .filters import SubjectFilter
from .models import Subject
from .serializers import SubjectSerializer


class SubjectList(ListCreateAPIView):
    serializer_class = SubjectSerializer
    queryset = Subject.objects.all()

    def perform_create(self, serializer):
        serializer.save()

    def get_queryset(self):
        return self.queryset.all()


class SubjectDetailAPIView(RetrieveUpdateDestroyAPIView):
    serializer_class = SubjectSerializer
    queryset = Subject.objects.all()
    lookup_field = "id"

    def get_queryset(self):
        return self.queryset.all()

from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView

from .filters import ProfessorFilter
from .models import Professor
from .serializers import ProfessorSerializer


class ProfessorList(ListCreateAPIView):
    serializer_class = ProfessorSerializer
    queryset = Professor.objects.all()

    def perform_create(self, serializer):
        serializer.save()

    def get_queryset(self):
        return self.queryset.all()


class ProfessorDetailAPIView(RetrieveUpdateDestroyAPIView):
    serializer_class = ProfessorSerializer
    queryset = Professor.objects.all()
    lookup_field = "id"

    def get_queryset(self):
        return self.queryset.all()

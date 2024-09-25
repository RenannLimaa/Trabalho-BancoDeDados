from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView

from .filters import GradeFilter
from .models import Grade
from .serializers import GradeSerializer


class GradeList(ListCreateAPIView):
    serializer_class = GradeSerializer
    queryset = Grade.objects.all()

    def perform_create(self, serializer):
        serializer.save()

    def get_queryset(self):
        return self.queryset.all()


class GradeDetailAPIView(RetrieveUpdateDestroyAPIView):
    serializer_class = GradeSerializer
    queryset = Grade.objects.all()
    lookup_field = "id"

    def get_queryset(self):
        return self.queryset.all()

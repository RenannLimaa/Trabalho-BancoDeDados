from django.views.generic import G
from rest_framework.viewsets import GenericViewSet

from .filters import ClassFilter
from .models import Class
from .serializers import ClassSerializer


class ClassViewSet(GenericViewSet):
    queryset = Class.objects.all().order_by("-id")
    serializer_class = ClassSerializer
    filterset_class = ClassFilter

from django_filters import BaseFilterSet, CharFilter

from .models import Course


class CourseFilter(BaseFilterSet):
    class Meta:
        model = Course
        fields = ["name", "description"]
        search_fields = ["name", "description"]

    name = CharFilter(lookup_expr="icontains")
    description = CharFilter(lookup_expr="icontains")

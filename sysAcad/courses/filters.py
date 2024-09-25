from django_filters import CharFilter, FilterSet

from .models import Course


class CourseFilter(FilterSet):
    class Meta:
        model = Course
        fields = ["name", "description"]
        search_fields = ["name", "description"]

    name = CharFilter(lookup_expr="icontains")
    description = CharFilter(lookup_expr="icontains")

from django_filters import BaseFilterSet, CharFilter, NumberFilter

from .models import Subject


class SubjectFilter(BaseFilterSet):
    class Meta:
        model = Subject
        fields = ["name", "description", "course"]
        search_fields = ["name", "description", "course__name"]

    name = CharFilter(lookup_expr="icontains")
    description = CharFilter(lookup_expr="icontains")
    course = NumberFilter(field_name="course__id")

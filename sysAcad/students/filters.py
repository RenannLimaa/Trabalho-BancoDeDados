from django_filters import BaseFilterSet, CharFilter, NumberFilter

from .models import Student


class StudentFilter(BaseFilterSet):
    class Meta:
        model = Student
        fields = ["name", "email", "celphone"]
        search_fields = ["name", "email", "celphone"]

    name = CharFilter(lookup_expr="icontains")

    email = CharFilter(lookup_expr="icontains")

    cellphone = NumberFilter()

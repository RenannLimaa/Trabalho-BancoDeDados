from django_filters import CharFilter, FilterSet, NumberFilter

from .models import Student


class StudentFilter(FilterSet):
    class Meta:
        model = Student
        fields = ["name", "email", "cellphone"]
        search_fields = ["name", "email", "cellphone"]

    name = CharFilter(lookup_expr="icontains")

    email = CharFilter(lookup_expr="icontains")

    cellphone = NumberFilter()

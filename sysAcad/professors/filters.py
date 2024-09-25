from django_filters import CharFilter, FilterSet, NumberFilter

from .models import Professor


class ProfessorFilter(FilterSet):
    class Meta:
        model = Professor
        fields = ["name", "email", "cellphone"]
        search_fields = ["name", "email", "cellphone"]

    name = CharFilter(lookup_expr="icontains")

    email = CharFilter(lookup_expr="icontains")

    cellphone = NumberFilter()

from django_filters import BaseFilterSet, NumberFilter

from .models import Grade


class GradeFilter(BaseFilterSet):
    class Meta:
        model = Grade
        fields = ["student", "subject", "grade1", "grade2", "grade3"]
        search_fields = ["student__name", "subject__name"]

    student = NumberFilter(field_name="student__id")
    subject = NumberFilter(field_name="subject__id")
    grade1 = NumberFilter()
    grade2 = NumberFilter()
    grade3 = NumberFilter()

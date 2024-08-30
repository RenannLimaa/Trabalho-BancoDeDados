from django_filters import BaseFilterSet, CharFilter, NumberFilter

from .models import Class


class ClassFilter(BaseFilterSet):
    class Meta:
        model = Class
        fields = ["subject", "room", "schedule", "seat_count"]
        search_fields = ["subject__name", "room", "schedule"]

    subject = NumberFilter(field_name="subject__id")
    room = CharFilter(lookup_expr="icontains")
    schedule = CharFilter(lookup_expr="icontains")
    seat_count = NumberFilter()

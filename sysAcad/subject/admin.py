from django.contrib import admin
from .models import Subject


@admin.register(Subject)
class SubjectAdmin(admin.ModelAdmin):
    list_display = ('name', 'vacancies', 'course')
    search_fields = ('name', 'course__name')

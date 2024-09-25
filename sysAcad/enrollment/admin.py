from django.contrib import admin
from .models import Enrollment

@admin.register(Enrollment)
class EnrollmentAdmin(admin.ModelAdmin):
    list_display = ('student', 'course', 'get_subjects')
    search_fields = ('student__user__username', 'course__name')

    def get_subjects(self, obj):
        return ", ".join(subject.name for subject in obj.subjects.all())
    get_subjects.short_description = 'Subjects'

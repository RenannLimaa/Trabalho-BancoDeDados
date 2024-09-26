from django.contrib import admin
from .models import Enrollment

class EnrollmentAdmin(admin.ModelAdmin):
    search_fields = ('student__user__username', 'course__name')

admin.site.register(Enrollment, EnrollmentAdmin)

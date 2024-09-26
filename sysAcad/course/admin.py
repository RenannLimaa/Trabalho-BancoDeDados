from django.contrib import admin
from .models import Course

class CourseAdmin(admin.ModelAdmin):
    list_display = ('name', 'duration')
    search_fields = ('name', 'duration')

admin.site.register(Course, CourseAdmin)

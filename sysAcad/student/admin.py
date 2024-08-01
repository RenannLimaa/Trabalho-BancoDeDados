from django.contrib import admin

from .models import Student


class StudentAdmin(admin.ModelAdmin):
    list_display = ('registration', 'name', 'email', 'cellphone', 'birth_date')
    search_fields = ('name', 'email', 'registration')


admin.site.register(Student, StudentAdmin)

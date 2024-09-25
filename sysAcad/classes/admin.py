from django.contrib import admin
from .models import Classes  


class ClassAdmin(admin.ModelAdmin):
    list_display = ('classroom', 'start_time', 'day_of_week', 'end_time', 'subject', 'professor')
    list_filter = ('subject', 'professor', 'day_of_week')
    fields = ('classroom', 'start_time', 'day_of_week', 'end_time', 'subject', 'professor')

admin.site.register(Classes, ClassAdmin)

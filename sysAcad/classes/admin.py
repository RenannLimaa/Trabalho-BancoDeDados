from django.contrib import admin

from classes.models import Classes, Day


class ClassesAdmin(admin.ModelAdmin):
    filter_horizontal = ('days_of_week',)
    list_filter = ('subject', 'professor', 'days_of_week')

    fieldsets = (
        ('General Information', {
            'fields': ('subject', 'professor', 'classroom', 'vacancies')
        }),

        ('Schedule', {
            'fields': ('days_of_week', 'start_time', 'end_time')
        })
    )

    
admin.site.register(Classes, ClassesAdmin)
admin.site.register(Day)

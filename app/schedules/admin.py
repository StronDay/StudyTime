from django.contrib import admin
from .models import Schedule

@admin.register(Schedule)
class ScheduleAdmin(admin.ModelAdmin):
    list_display = ('day_of_week', 'start_time', 'end_time', 'subject', 'group', 'teacher', 'classroom')
    list_filter = ('day_of_week', 'group', 'teacher')
    search_fields = ('subject', 'teacher', 'classroom')
    ordering = ('day_of_week', 'start_time')
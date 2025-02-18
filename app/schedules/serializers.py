from rest_framework import serializers
from .models import Schedule

class ScheduleSerializer(serializers.ModelSerializer):
    day_of_week = serializers.CharField(source='get_day_of_week_display')
    
    class Meta:
        model = Schedule
        fields = [
            'id',
            'day_of_week',
            'start_time',
            'end_time',
            'subject',
            'teacher',
            'classroom',
            'additional_info'
        ]
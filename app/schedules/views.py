from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from .models import Schedule
from students.models import StudentInfo
from .serializers import ScheduleSerializer

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def get_schedule(request):
    try:
        student_info = StudentInfo.objects.get(user=request.user)
        group = student_info.group
        day_of_week = request.GET.get('day', None)
        
        schedules = Schedule.objects.filter(group=group)
        
        if day_of_week:
            schedules = schedules.filter(day_of_week=day_of_week)
            
        serializer = ScheduleSerializer(schedules, many=True)
        return Response(serializer.data)
        
    except StudentInfo.DoesNotExist:
        return Response({'error': 'Student profile not found'}, status=404)
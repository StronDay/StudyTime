from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from rest_framework.exceptions import NotFound
from django.contrib.auth import get_user_model

from .models import StudentInfo
from .serializers import StudentInfoSerializer

from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
    
class StudentInfoApiView(generics.ListCreateAPIView):
    queryset = StudentInfo.objects.all()
    serializer_class = StudentInfoSerializer
    permission_classes = [IsAuthenticated]
    
# class StudentDetailApiView(generics.RetrieveAPIView):
#     serializer_class = StudentInfoSerializer
#     permission_classes = [IsAuthenticated]
#     lookup_field = 'user_id'  # Ключевое изменение
#     lookup_url_kwarg = 'user_id'  # Ключевое изменение

#     def get_object(self):
#         try:
#             user = get_user_model().objects.get(id=self.kwargs['user_id'])
#             return StudentInfo.objects.get(user=user)
#         except (get_user_model().DoesNotExist, StudentInfo.DoesNotExist):
#             raise NotFound("Student not found")

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def current_student(request):
    try:
        student_info = StudentInfo.objects.get(user=request.user)
        serializer = StudentInfoSerializer(student_info)
        return Response(serializer.data)
    except StudentInfo.DoesNotExist:
        return Response({'error': 'Student profile not found'}, status=404)
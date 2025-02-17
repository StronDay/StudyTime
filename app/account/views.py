from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import permission_classes
from .models import User
from .serializers import UserSerializer

@api_view(['GET'])
# @permission_classes([IsAuthenticated])
def get_user_info(request, user_id=None):
    if user_id:
        try:
            user = User.objects.get(user_id=user_id)
        except User.DoesNotExist:
            return Response({'error': 'User not found'}, status=404)
    else:
        user = request.user
    serializer = UserSerializer(user)
    return Response(serializer.data)
from django.urls import path
from .views import get_user_info

urlpatterns = [
    path('api/user-info/<str:user_id>/', get_user_info, name='user_info_by_id'),
]
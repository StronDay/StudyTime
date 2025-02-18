from django.urls import path
from .views import get_schedule

urlpatterns = [
    path('get/', get_schedule, name='get_schedule'),
]
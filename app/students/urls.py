from django.urls import path
from .views import StudentInfoApiView, current_student

urlpatterns = [
    path('get_all/', StudentInfoApiView.as_view()),
    path('current/', current_student, name='current-student'),
]
from rest_framework import serializers
from django.contrib.auth.models import User
from .models import StudentInfo, Group, Course

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name')

class GroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = Group
        fields = ['group']

class CourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = ['course']

class StudentInfoSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)
    group = GroupSerializer()
    course = CourseSerializer()

    class Meta:
        model = StudentInfo
        fields = ('group', 'course', 'user')
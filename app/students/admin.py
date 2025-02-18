from django.contrib import admin
from .models import StudentInfo, Group, Course

@admin.register(StudentInfo)
class StudentInfoAdmin(admin.ModelAdmin):
    list_display = ('get_firstname', 'get_lastname', 'group', 'course', 'get_username')
    search_fields = ('group', 'course')
    
    def get_username(self, obj):
        return obj.user.username
    get_username.short_description = 'Username'
    
    def get_firstname(self, obj):
        return obj.user.first_name
    get_username.short_description = 'FirstName'
    
    def get_lastname(self, obj):
        return obj.user.last_name
    get_username.short_description = 'LastName'

admin.site.register(Group)
admin.site.register(Course)



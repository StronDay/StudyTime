from django.contrib.auth import get_user_model
from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
    
class StudentInfo(models.Model):
    
    class Meta:
        db_table = 'students_info'
        
    user = models.OneToOneField(get_user_model(), on_delete=models.CASCADE)
        
    group = models.ForeignKey('Group', on_delete=models.PROTECT)
    course = models.ForeignKey('Course', on_delete=models.PROTECT)

    def __str__(self):
        return f"{self.user.username}"
    
class Group(models.Model):
    
    class Meta:
        db_table = 'groups'
        
    group = models.CharField(max_length=30)
    
    def __str__(self):
        return self.group

class Course(models.Model):
    
    class Meta:
        db_table = 'courses'
        
    course = models.PositiveSmallIntegerField(validators=[MinValueValidator(1), MaxValueValidator(6)])
    
    def __str__(self):
        return str(self.course)


# from django.db import models
# from django.core.validators import MinValueValidator, MaxValueValidator
# import uuid

# from abc import abstractmethod

# class User(models.Model):
    
#     class Meta:
#         abstract = True
        
#     STUDENT = 'STUDENT'
#     TEACHER = 'TEACHER'
#     UNKNOWN = 'UNKNOWN'

#     USER_ROLE = [
#         (UNKNOWN, "Неизвестно"), 
#         (STUDENT, "Студент"), 
#         (TEACHER, "Преподаватель")
#     ]
        
#     user_id = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)
#     user_role = models.CharField(max_length=30, choices=USER_ROLE, blank=False, null=False, editable=False)
    
#     first_name = models.CharField(max_length=30)
#     last_name = models.CharField(max_length=30)
#     login = models.CharField(max_length=30, unique=True)
#     password = models.CharField(max_length=100)
    
#     @abstractmethod
#     def get_role(self):
#         pass
    
#     def save(self, *args, **kwargs):
#         if not self.user_role:
#             self.user_role = self.get_role()
#         super().save(*args, **kwargs) 

#     def __str__(self):
#         return self.login
    
# class Student(User):
    
#     class Meta:
#         db_table = 'students'
        
#     group = models.ForeignKey('Group', on_delete=models.PROTECT)
#     course = models.ForeignKey('Course', on_delete=models.PROTECT)
    
#     def get_role(self):
#         return self.STUDENT

#     def __str__(self):
#         return f"{self.login}"

# class Teacher(User):
    
#     class Meta:
#         db_table = 'teachers'
    
#     def get_role(self):
#         return self.TEACHER

#     def __str__(self):
#         return f"{self.login}"
    
# class Group(models.Model):
    
#     class Meta:
#         db_table = 'groups'
        
#     group = models.CharField(max_length=30)
    
#     def __str__(self):
#         return self.group

# class Course(models.Model):
    
#     class Meta:
#         db_table = 'courses'
        
#     course = models.PositiveSmallIntegerField(validators=[MinValueValidator(1), MaxValueValidator(6)])
    
#     def __str__(self):
#         return str(self.course)

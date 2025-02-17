from django.db import models
import uuid

class User(models.Model):
    id = models.AutoField(primary_key=True)
    user_id = models.CharField(max_length=100, unique=True, default=uuid.uuid4)
    login = models.CharField(max_length=30, unique=True)
    password = models.CharField(max_length=100)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)

    def __str__(self):
        return self.login
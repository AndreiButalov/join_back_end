from django.contrib.auth.models import User
from django.db import models

class UserProfile(models.Model):    
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True, related_name='profile')
    color = models.CharField(max_length=50, default='red')

    def __str__(self):
        return self.user.username
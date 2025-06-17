from django.db import models
from user_auth_app.models import UserProfile

class GuestContact(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=20)
    color = models.CharField(max_length=20)

    def __str__(self):
        return self.name



class SubTask(models.Model):
    content = models.CharField(max_length=255)
    is_done = models.BooleanField(default=False)
    task = models.ForeignKey("Task", on_delete=models.CASCADE, null=True, related_name='subtasks')

    def __str__(self):
        return self.content



class Task(models.Model):
   
    title = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    category = models.CharField(max_length=20, null=True, blank=True)
    priority = models.CharField(max_length=20, default="Medium")    
    priorityImg = models.TextField(default="./assets/img/vector_strich.svg") 
    status = models.CharField(max_length=50)
    date = models.DateField()    
    assigned_user = models.ForeignKey(UserProfile, on_delete=models.SET_NULL, null=True, blank=True, related_name='tasks')
    assigned_guests = models.ManyToManyField(GuestContact, blank=True, related_name='tasks')   
    is_selected = models.BooleanField(default=False)

    def __str__(self):
        return self.title

    
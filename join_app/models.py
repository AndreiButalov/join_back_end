from django.db import models

class User(models.Model):
    color = models.CharField(max_length=20)
    email = models.EmailField()
    name = models.CharField(max_length=100)
    password = models.TextField()


    def __str__(self):
        return self.name



class GuestContact(models.Model):
    # user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='guest_contacts')
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=20)
    color = models.CharField(max_length=20)

    def __str__(self):
        return self.name



class SubTask(models.Model):
    content = models.CharField(max_length=255)
    is_done = models.BooleanField(default=False)

    def __str__(self):
        return self.content



class Task(models.Model):
   
    # name = models.ManyToManyField(GuestContact, blank=True, related_name='guest_contacts')
    title = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    category = models.CharField(max_length=20, null=True, blank=True)
    priority = models.CharField(max_length=20, default="Medium")    
    priorityImg = models.TextField(default="./assets/img/vector_strich.svg") 
    status = models.CharField(max_length=50)
    date = models.DateField()
    subtasks = models.ManyToManyField(SubTask, blank=True)
    # assigned_users = models.ManyToManyField(User, blank=True, related_name='tasks')
    assigned_guests = models.ManyToManyField(GuestContact, blank=True, related_name='tasks')
    

    is_selected = models.BooleanField(default=False)

    def __str__(self):
        return self.title

    # def save(self, *args, **kwargs):        
    #     if not self.initial and self.assigned_guests.exists():
    #         first_guest = self.assigned_guests.first()
    #         self.initial = first_guest.name[:2].upper()
    #         self.color = first_guest.color
    #     super().save(*args, **kwargs)

from django.contrib import admin
from .models import UserProfile, GuestContact, SubTask, Task

admin.site.register(UserProfile)
admin.site.register(GuestContact)
admin.site.register(SubTask)
admin.site.register(Task)

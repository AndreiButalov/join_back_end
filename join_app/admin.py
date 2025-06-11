from django.contrib import admin
from .models import User, GuestContact, SubTask, Task

admin.site.register(User)
admin.site.register(GuestContact)
admin.site.register(SubTask)
admin.site.register(Task)

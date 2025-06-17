from rest_framework import serializers
from join_app.models import GuestContact, Task, SubTask

class GuestContactsSerializer(serializers.ModelSerializer):
    class Meta:
        model = GuestContact
        fields = '__all__'


class TasksSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = '__all__'


class SubTaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = SubTask
        fields = '__all__'
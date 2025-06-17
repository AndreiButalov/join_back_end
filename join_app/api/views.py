from rest_framework.decorators import api_view
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import UserProfileSerializer, GuestContactsSerializer, TasksSerializer, SubTaskSerializer
from join_app.models import UserProfile, GuestContact, Task, SubTask
from rest_framework import mixins
from rest_framework import generics
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from rest_framework.permissions import AllowAny
from rest_framework.views import APIView


class UsersView(mixins.ListModelMixin, mixins.CreateModelMixin, generics.GenericAPIView):
    
    queryset = UserProfile.objects.all()
    serializer_class = UserProfileSerializer

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)
    


class UsersDetail(mixins.RetrieveModelMixin,
                  mixins.UpdateModelMixin,
                  mixins.DestroyModelMixin,
                  generics.GenericAPIView):
    queryset = UserProfile.objects.all()
    serializer_class = UserProfileSerializer

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def patch(self, request, *args, **kwargs):
        return self.partial_update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)
    


class GuestContactsView(mixins.ListModelMixin, mixins.CreateModelMixin, generics.GenericAPIView):
    
    queryset = GuestContact.objects.all()
    serializer_class = GuestContactsSerializer

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

  
class TasksView(mixins.ListModelMixin, mixins.CreateModelMixin, generics.GenericAPIView):
    
    queryset = Task.objects.all()
    serializer_class = TasksSerializer

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)  
      
    def patch(self, request, *args, **kwargs):
        return self.partial_update(request, *args, **kwargs)   
    

class TasksDetail(mixins.RetrieveModelMixin,
                  mixins.UpdateModelMixin,
                  mixins.DestroyModelMixin,
                  generics.GenericAPIView):
    queryset = Task.objects.all()
    serializer_class = TasksSerializer

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def patch(self, request, *args, **kwargs):
        return self.partial_update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)


class GuestContactsDetail(mixins.RetrieveModelMixin,
                  mixins.UpdateModelMixin,
                  mixins.DestroyModelMixin,
                  generics.GenericAPIView):
    queryset = GuestContact.objects.all()
    serializer_class = GuestContactsSerializer

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def patch(self, request, *args, **kwargs):
        return self.partial_update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)
    

class SubTasksView(mixins.ListModelMixin, mixins.CreateModelMixin, generics.GenericAPIView):
    
    queryset = SubTask.objects.all()
    serializer_class = SubTaskSerializer

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)  
      
    def patch(self, request, *args, **kwargs):
        return self.partial_update(request, *args, **kwargs)  
    

class SubTasksDetail(mixins.RetrieveModelMixin,
                  mixins.UpdateModelMixin,
                  mixins.DestroyModelMixin,
                  generics.GenericAPIView):
    queryset = SubTask.objects.all()
    serializer_class = SubTaskSerializer

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def patch(self, request, *args, **kwargs):
        return self.partial_update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)
    

class LoginView(APIView):
    
    permission_classes = [AllowAny]

    def post(self, request):
        email = request.data.get('email')
        password = request.data.get('password')

        print(email)
        print(password)

        try:
            user = User.objects.get(email=email)
        except User.DoesNotExist:
            return Response({'error': 'E-Mail nicht gefunden'}, status=404)

        user = authenticate(username=user.username, password=password)
        if user is not None:
            profile = UserProfile.objects.get(user=user)
            serializer = UserProfileSerializer(profile)
            return Response(serializer.data)
        return Response({'error': 'Falsches Passwort'}, status=401)
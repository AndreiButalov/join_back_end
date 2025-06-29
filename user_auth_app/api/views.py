from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import generics, mixins
from django.contrib.auth import authenticate
from user_auth_app.models import UserProfile
from .serializers import UserProfileSerializer
from django.contrib.auth.models import User
from rest_framework.permissions import AllowAny
from .serializers import RegistrationSerializer
from rest_framework.authtoken.models import Token


from rest_framework.authtoken.models import Token

class LoginView(APIView):
    permission_classes = [AllowAny]

    def post(self, request):
        email = request.data.get('email')
        password = request.data.get('password')

        try:
            user = User.objects.get(email=email)
        except User.DoesNotExist:
            return Response({'error': 'E-Mail nicht gefunden'}, status=404)

        user = authenticate(username=user.username, password=password)
        if user is not None:
            token, _ = Token.objects.get_or_create(user=user)
            profile = UserProfile.objects.get(user=user)
            serializer = UserProfileSerializer(profile)

            return Response({
                'token': token.key,
                'user': serializer.data
            }, status=200)

        return Response({'error': 'Falsches Passwort'}, status=401)



class RegisterView(APIView):
    permission_classes = [AllowAny]

    def post(self, request):
        serialzer = RegistrationSerializer(data=request.data)
        data  = {}

        if serialzer.is_valid():
            saved_account = serialzer.save()
            token, _ = Token.objects.get_or_create(user=saved_account)
            data  = {
                'token': token.key,
                'username': saved_account.username,
                'email': saved_account.email
            }
        else:
            data=serialzer.errors

        return Response(data)







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

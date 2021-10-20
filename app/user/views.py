from django.shortcuts import render
from rest_framework import generics, authentication, permissions
from user.serializers import AuthTokenSerializer, UserSerializer, AuthTokenSerializer
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.settings import api_settings


class CreateUserView(generics.CreateAPIView):
    #Create a new user in the system
    serializer_class = UserSerializer
    

class CreateTokenview(ObtainAuthToken):
    #Create a ne auth token for user
    serializer_class = AuthTokenSerializer
    render_classes = api_settings.DEFAULT_RENDERER_CLASSES


class ManageUserView(generics.RetrieveUpdateAPIView):
    #Manage the auth of the user
    serializer_class = UserSerializer
    authentication_classes = (authentication.TokenAuthentication,)
    permissions_classes = (permissions.IsAuthenticated,)

    def get_object(self):
        return self.request.user
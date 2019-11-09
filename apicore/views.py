from rest_framework import generics, permissions
from rest_framework.authentication import TokenAuthentication
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from django.contrib.auth.models import User
from .models import Extension, Career, UserProfile, Server, ServerUser
from .serializers import ExtensionSerializer, CareerSerializer, ProfileSerializer, UserSerializer, ServerSerializer, ServerUserSerializer
from .permissions import IsOwnerOrReadOnly


# Create your views here.
class ExtensionList(generics.ListCreateAPIView):
    queryset = Extension.objects.all()
    serializer_class = ExtensionSerializer
    # permission_classes = (permissions.IsAuthenticatedOrReadOnly,)
    # authentication_classes = (SessionAuthentication, TokenAuthentication, BasicAuthentication,) 

class ExtensionDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Extension.objects.all()
    serializer_class = ExtensionSerializer
    # permission_classes = (permissions.IsAuthenticated,)
    # authentication_classes = (SessionAuthentication, TokenAuthentication, BasicAuthentication,) 

class CareerList(generics.ListCreateAPIView):
    queryset = Career.objects.all()
    serializer_class = CareerSerializer

class CareerDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Career.objects.all()
    serializer_class = CareerSerializer
    

class ProfileList(generics.ListCreateAPIView):
    queryset = UserProfile.objects.all()
    serializer_class = ProfileSerializer
    # permission_classes = (permissions.IsAuthenticatedOrReadOnly,)
    # authentication_classes = (SessionAuthentication, TokenAuthentication, BasicAuthentication,) 

class ProfileDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = UserProfile.objects.all()
    serializer_class = ProfileSerializer
    permission_classes = (IsOwnerOrReadOnly,)
    # authentication_classes = (SessionAuthentication, TokenAuthentication, BasicAuthentication,)     

class UserList(generics.ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    def get_permissions(self):
        permission_classes = []
        if self.request.method == 'POST':
            permission_classes = [permissions.AllowAny]

        return [permission() for permission in permission_classes]
    # permission_classes = (permissions.IsAuthenticated)
    # authentication_classes = (AllowAny,)

class UserDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = (IsOwnerOrReadOnly,)
    # authentication_classes = (TokenAuthentication,)
    # permission_classes = (permissions.IsAuthenticated, IsOwnerOrReadOnly,)

class ServerList(generics.ListCreateAPIView):
    queryset = Server.objects.all()
    serializer_class = ServerSerializer

class ServerDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Server.objects.all()
    serializer_class = ServerSerializer


class ServerUserList(generics.ListCreateAPIView):
    queryset = ServerUser.objects.all()
    serializer_class = ServerUserSerializer

class ServerUserDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = ServerUser.objects.all()
    serializer_class = ServerUserSerializer

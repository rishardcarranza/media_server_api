from rest_framework import generics, permissions
from rest_framework.authentication import TokenAuthentication
from django.contrib.auth.models import User
from .models import Extension, Profile
from .serializers import ExtensionSerializer, ProfileSerializer, UserSerializer
from .permissions import IsOwnerOrReadOnly


# Create your views here.
class ExtensionList(generics.ListCreateAPIView):
    """
    Extension class
    """
    queryset = Extension.objects.all()
    serializer_class = ExtensionSerializer
    # permission_classes = (permissions.IsAuthenticatedOrReadOnly,)
    # authentication_classes = (SessionAuthentication, TokenAuthentication, BasicAuthentication,) 

class ExtensionDetail(generics.RetrieveUpdateDestroyAPIView):
    """
    Extension class
    """
    queryset = Extension.objects.all()
    serializer_class = ExtensionSerializer
    # permission_classes = (permissions.IsAuthenticated,)
    # authentication_classes = (SessionAuthentication, TokenAuthentication, BasicAuthentication,) 

class ProfileList(generics.ListCreateAPIView):
    """
    Profile class
    """
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer
    # permission_classes = (permissions.IsAuthenticatedOrReadOnly,)
    # authentication_classes = (SessionAuthentication, TokenAuthentication, BasicAuthentication,) 

class ProfileDetail(generics.RetrieveUpdateDestroyAPIView):
    """
    Profile class
    """
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer
    permission_classes = (IsOwnerOrReadOnly,)
    # authentication_classes = (SessionAuthentication, TokenAuthentication, BasicAuthentication,)     

class UserList(generics.ListCreateAPIView):
    """
    User class
    """
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = (permissions.IsAuthenticated,)
    # authentication_classes = (AllowAny,)

class UserDetail(generics.RetrieveUpdateDestroyAPIView):
    """
    User class
    """
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = (IsOwnerOrReadOnly,)
    # authentication_classes = (TokenAuthentication,)
    # permission_classes = (permissions.IsAuthenticated, IsOwnerOrReadOnly,)

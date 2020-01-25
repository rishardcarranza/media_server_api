import socket, os
from rest_framework import generics, permissions
from rest_framework.authentication import TokenAuthentication
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from django.conf import settings
from django.contrib.auth.models import User
from .models import Extension, Career, UserProfile, Server, ServerUser, CommandServer, FilesUser
from .serializers import ExtensionSerializer, CareerSerializer, ProfileSerializer, UserSerializer, ServerSerializer, ServerUserSerializer, LocalServerSerializer, CommandServerSerializer, FilesUserSerializer
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

class FilesUserList(generics.ListCreateAPIView):
    queryset = FilesUser.objects.all()
    serializer_class = FilesUserSerializer

    def perform_create(self, serializer):
        # Include the owner attribute directly, rather than from request data.
        instance = serializer.save()
        # Perform a custom post-save action.
        media_path = settings.MEDIA_ROOT
        filename = instance.file
        file_path = media_path+"/"+str(filename)
        content_type = self.request.FILES['file'].content_type

        if 'audio' in str(content_type):
            print('Archivo de audio')
            # Get the command from DB
            _exec = CommandServer.objects.get(action="open-audio")
            os.system(_exec.command.format(file_path))
        elif 'video' in str(content_type):
            print('Archivo de video')
            _exec = CommandServer.objects.get(action="open-video")
            os.system(_exec.command.format(file_path))
        elif 'image' in str(content_type):
            print('Archivo de imagen')
            _exec = CommandServer.objects.get(action="open-image")
            os.system(_exec.command.format(file_path))
        elif 'application' in str(content_type) and 'presentation' in str(content_type):
            print('Archivo de presentacion en power point')
            _exec = CommandServer.objects.get(action="open-presentation")
            os.system(_exec.command.format(file_path))
        else:
            print('Archivo no soportado')

        # os.system('open /Users/rishardcarranza/Environments/django/media_server/media/files/'+str(filename))
        # print('Post save File action', self.request.FILES['file'].content_type, self.request.user)
        
        # send_email(instance.to_email, instance.message)

class FilesUserDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = FilesUser.objects.all()
    serializer_class = FilesUserSerializer

class LocalServerView(APIView):
    
    def post(self, request):
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.connect(("8.8.8.8", 80))
        loca_ip = s.getsockname()[0]

        yourdata = [{"ipaddr": loca_ip, "user_request": request.user}]
        results = LocalServerSerializer(yourdata, many=True).data
        return Response(results)

class CommandServerView(APIView):
    execute = ""
    action = ""

    def post(self, request):
        if request.data:
            print(request.data)
            action = request.data["action"]
            value = request.data["value"]
            # Get the command from DB
            _exec = CommandServer.objects.get(action=action)
            exec_command = ""
            
            # Whats option to execute
            if value != "":
                os.system(_exec.command.format(value))
                exec_command = _exec.command.format(value)
            else:
                os.system(_exec.command)
                exec_command = _exec.command

            # if action == "volume":
            #     os.system(_exec.command.format(value))
            # elif action == "display":
            #     os.system(_exec.command.format(value))
            # elif action == "poweroff":
            #     os.system(_exec.command)
            # elif action == "reboot":
            #     os.system(_exec.command)
            # elif action == "play":
            #     os.system(_exec.command)
            # elif action == "pause":
            #     os.system(_exec.command)
            # elif action == "stop":
            #     os.system(_exec.command)
            # elif action == "open-video":
            #     os.system(_exec.command.format(value))
            # elif action == "open-audio":
            #     os.system(_exec.command.format(value))
            # elif action == "open-image":
            #     os.system(_exec.command.format(value))
            # elif action == "open-presentation":
            #     os.system(_exec.command.format(value))
            # elif action == "next-slide":
            #     os.system(_exec.command)
            # elif action == "prev-slide":
            #     os.system(_exec.command)
            # else:
            #     pass            

        response_data = [{"status": True, "command": exec_command, "user_request": request.user}]
        results = CommandServerSerializer(response_data, many=True).data

        return Response(results)
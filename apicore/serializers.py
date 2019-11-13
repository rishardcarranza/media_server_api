from rest_framework import serializers
from django.contrib.auth.models import User
from django.contrib.auth.hashers import make_password
from rest_framework.authtoken.models import Token
from .models import Extension, Career, UserProfile, Career, Server, ServerUser


class UserSerializer(serializers.ModelSerializer):
    # avatar = serializers.URLField(source='profile.avatar', read_only=False)

    class Meta:
        model = User
        fields = ('id', 'username', 'password', 'first_name', 'last_name', 'email', 'is_active', 'date_joined', 'last_login')

    def create(self, validated_data):
        user = User.objects.create(
            username = validated_data['username'],
            password = make_password(validated_data['password']),
            email = validated_data['email'],
            first_name = validated_data['first_name'],
            last_name = validated_data['last_name'],
            is_active = True,
            is_staff = True,
        )

        return user

    def update(self, instance, validated_data):
        if instance.username == validated_data['username']:
            instance.email = validated_data['email']
            instance.first_name = validated_data['first_name']
            instance.last_name = validated_data['last_name']
            instance.is_active = validated_data['is_active']

            instance.save()
            return instance
        else:
            return "User not authorized"

class ProfileSerializer(serializers.ModelSerializer):
    # user = UserSerializer(required=True)
    class Meta:
        model = UserProfile
        fields = ('id', 'user', 'avatar', 'career')


class TokenSerializer(serializers.ModelSerializer):
    user = UserSerializer()
    class Meta:
        model = Token
        fields = ('key', 'user')

class ExtensionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Extension
        fields = ('id', 'name', 'status')

class CareerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Career
        fields = ('id', 'name', 'status')

class ServerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Server
        fields = ('id', 'hostname', 'ip_address', 'port', 'mac_address', 'volume', 'screen', 'pin')

class ServerUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = ServerUser
        fields = ('server', 'user', 'status', 'session', 'connect_date', 'last_date')

class LocalServerSerializer(serializers.Serializer):
    ipaddr = serializers.CharField()
    user_request = serializers.CharField()
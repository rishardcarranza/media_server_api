from rest_framework import serializers
from django.contrib.auth.models import User
from django.contrib.auth.hashers import make_password
from .models import Extension, Career, Profile, Career, Server, ServerUser


class UserSerializer(serializers.ModelSerializer):
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

    class Meta:
        model = User
        fields = ('id', 'username', 'password', 'first_name', 'last_name', 'email', 'is_active', 'date_joined', 'last_login')

class ExtensionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Extension
        fields = ('id', 'name', 'status')

class CareerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Career
        fields = ('id', 'name', 'status')

class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = ('id', 'user', 'avatar', 'career')

class ServerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Server
        fields = ('id', 'hostname', 'ip_address', 'port', 'mac_address', 'volume', 'screen', 'pin')

class ServerUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = ServerUser
        fields = ('server', 'user', 'status', 'session', 'connect_date', 'last_date')
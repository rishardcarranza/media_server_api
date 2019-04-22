from rest_framework import serializers
from django.contrib.auth.models import User
from django.contrib.auth.hashers import make_password
from .models import Extension, Profile


class UserSerializer(serializers.ModelSerializer):
    def create(self, validated_data):
        user = User.objects.create_user(
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

class ProfileSerializer(serializers.ModelSerializer):

    # def create(self, validated_data):
    #     print(validated_data)
    #     return Profile.objects.create(**validated_data)

    # def update(self, instance, validated_data):
    #     print(instance.__dict__)
    #     print(validated_data['avatar'].__dict__)
    #     instance.save()
    #     return instance


    class Meta:
        model = Profile
        fields = ('id', 'user', 'avatar')
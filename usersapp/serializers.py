from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Player

class UserListSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        exclude = ['password']

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["id", "username", "first_name", "email", "password"]

class PlayerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Player
        fields = "__all__"

class UserRegistrationSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'password']

class UserLoginSerializer(serializers.Serializer):
    class Meta:
        model = User
        fields = ['username', 'password']



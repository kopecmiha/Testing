from rest_framework import serializers
from .models import User


class DeanSingInSerializer(serializers.ModelSerializer):
    class Meta(object):
        model = User
        fields = "username", "email"
        extra_kwargs = {'password': {'write_only': True}}


class UserSerializer(serializers.ModelSerializer):
    class Meta(object):
        model = User
        fields = "username", "status"
        extra_kwargs = {'password': {'write_only': True}}


class UserProfileSerializer(serializers.ModelSerializer):
    class Meta(object):
        model = User
        fields = "uuid", "username", "status", "email", "first_name", "last_name", "patronymic", "avatar", "status"

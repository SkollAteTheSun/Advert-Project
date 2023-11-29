from rest_framework import serializers
from .models import *
from django.contrib.auth.hashers import make_password


class CustomUserSerializer(serializers.ModelSerializer):
    """
    Сериалайзер модели CustomUser для создания аккаунта
    """
    password = serializers.CharField(write_only=True)

    def create(self, validated_data):
        password = validated_data.pop('password')
        hashed_password = make_password(password)
        user = CustomUser.objects.create(password=hashed_password, **validated_data)
        return user

    class Meta:
        model = CustomUser
        fields = ('id', 'username', 'password', 'first_name', 'last_name',)
        extra_kwargs = {'password': {'write_only': True}}


class CustomUserLoginSerializer(serializers.ModelSerializer):
    """
    Сериалайзер модели CustomUser для входа в аккаунт
    """
    password = serializers.CharField(write_only=True)

    class Meta:
        model = CustomUser
        fields = ('username', 'password',)
        extra_kwargs = {'password': {'write_only': True}}

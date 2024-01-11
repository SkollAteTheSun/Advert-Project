from rest_framework import serializers
from django.contrib.auth.hashers import make_password
from django.contrib.auth.models import User

class UserSerializers(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'password', 'first_name', 'last_name',)
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        password = validated_data.pop('password', None)
        instance = super(UserSerializers, self).create(validated_data)
        if password is not None:
            instance.set_password(password)
        instance.save()
        return instance
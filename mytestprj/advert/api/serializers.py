from rest_framework import serializers
from .models import *


class CategorySerializer(serializers.ModelSerializer):
    """
    Сериалайзер модели Category
    """
    class Meta:
        model = Category
        fields = ['name']


class AdvertSerializer(serializers.ModelSerializer):
    """
    Сериалайзер модели Advert
    """
    class Meta:
        model = Advert
        fields = ['user', 'category', 'name', 'description', 'photo']


class ProposalSerializer(serializers.ModelSerializer):
    """
    Сериалайзер модели Proposal
    """
    class Meta:
        model = Proposal
        fields = ['user', 'advert', 'reward', 'comment', 'accepted']

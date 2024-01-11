from rest_framework import serializers
from .models import *


class CategorySerializer(serializers.ModelSerializer):

    class Meta:
        model = Category
        fields = ['name']


class AdvertSerializer(serializers.ModelSerializer):

    class Meta:
        model = Advert
        fields = ['user', 'category', 'name', 'description', 'photo']


class ProposalSerializer(serializers.ModelSerializer):

    class Meta:
        model = Proposal
        fields = ['user', 'advert', 'reward', 'comment', 'accepted']

from django.db.models import Max
from rest_framework import serializers
from .models import *


class CategorySerializer(serializers.ModelSerializer):

    class Meta:
        model = Category
        fields = ['name']


class ProposalSerializer(serializers.ModelSerializer):
    advert_info = serializers.SerializerMethodField()

    def get_advert_info(self, obj):
        return get_advert_info(obj)

    class Meta:
        model = Proposal
        fields = ['user', 'advert', 'reward', 'comment', 'accepted', 'advert_info']

def get_advert_info(obj):
    return {
        'num_proposals': Proposal.objects.filter(advert=obj.advert).count(),
        'max_reward': Proposal.objects.filter(advert=obj.advert).aggregate(Max('reward'))['reward__max']
    }

class AdvertSerializer(serializers.ModelSerializer):
        class Meta:
            model = Advert
            fields = ['user', 'categories', 'name', 'description', 'photo', 'published']

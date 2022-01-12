from django.db import models
from rest_framework import fields, serializers
from .models import Channel, Subscribe
from audios.models import Audio
from audios.serializers import AudioSerializer

class ChannelSerializer(serializers.ModelSerializer):
    class Meta:
        model= Channel
        fields = ['id', 'user_id', 'channel_name', 'description', 'profile_pic','rate','subscriber']
        read_only_fields = ['id', 'rate','subscriber']

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        channel_id = representation['id']
        podcasts = Audio.objects.filter(channel_id=channel_id)
        serializer = AudioSerializer(podcasts, many=True)
        audios = serializer.data

        representation['podcasts'] = audios

        return representation

# class PodcastSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Audio
#         fields = ['id', 'user_id', 'channel_id',
#                   'title', 'Description', 'path', 'poster']
#         read_only_fields = ['id']


class ChannelPodcastSerializer(serializers.ModelSerializer):
    
    class Meta:
        model= Channel
        # fields = '__all__'
        fields = ['id', 'user_id', 'channel_name', 'description', 'profile_pic','rate','subscriber','podcasts']
        read_only_fields = ['id', 'rate','subscriber']


class SubscribeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Subscribe
        fields = ['id', 'user_id', 'channel_id', 'notification']
        read_only_fields = ['id']
        # depth = 1
    
    # def to_representation(self, instance):
    #     representation = super().to_representation(instance)
    #     user = representation['user_id']
    #     del representation['user_id']
    #     representation['user_id'] = user['id']
    #     return representation



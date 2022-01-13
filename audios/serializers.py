import re
from rest_framework import fields, serializers

from channels.models import Channel
from .models import Audio
import random

class AudioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Audio
        fields = ['id', 'user_id', 'channel_id',
                  'title', 'Description', 'path', 'poster','name']
        read_only_fields = ['id']

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        representation['numberOfListeners'] =  random.randint(0,10)
        representation['url'] = representation['path']
        representation['description'] = representation['Description']

        # print(instance.channel_id.id)
        channelId = instance.channel_id.id
        channel = Channel.objects.filter(id=channelId).first()
        # print(channel)
        representation['channelName'] = channel.channel_name
        return representation
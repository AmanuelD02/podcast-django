from rest_framework import fields, serializers
from .models import Channel, Subscribe


class ChannelSerializer(serializers.ModelSerializer):
    class Meta:
        model= Channel
        fields = ['id', 'user_id', 'channel_name', 'description', 'profile_pic','rate']
        read_only_fields = ['id', 'rate']


class SubscribeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Subscribe
        fields = ['id', 'user_id', 'channel_id', 'notification']
        read_only_fields = ['id']
        depth = 1
    
    def to_representation(self, instance):
        representation = super().to_representation(instance)
        user = representation['user_id']
        del representation['user_id']
        representation['user_id'] = user['id']
        return representation



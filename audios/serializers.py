from rest_framework import fields, serializers
from .models import Audio


class AudioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Audio
        fields = ['id', 'user_id', 'channel_id',
                  'title', 'Description', 'path', 'poster']
        read_only_fields = ['id']

        # def create(self, validated_data):
        #     audio = Audio(user_id=validated_data['user_id'], channel_id=validated_data['channel_id'], title=validated_data['title'],
        #                   decripttion=validated_data['description'], path=validated_data['path'], poster=validated_data['poster'])

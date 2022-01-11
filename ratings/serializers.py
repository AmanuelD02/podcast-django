from rest_framework import fields, serializers
from .models import Rating

class RatingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Rating
        fields = ['id','channel_id','user_id','rating']
        read_only_fields = ['id']
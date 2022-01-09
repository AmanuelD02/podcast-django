from django.shortcuts import render
from audios.models import Audio
from rest_framework import serializers
from rest_framework.views import APIView
from django.shortcuts import get_object_or_404
from rest_framework.response import Response

from audios.serializers import AudioSerializer
from rest_framework.permissions import AllowAny

# Create your views here.
class PostPodcastView(APIView):
    def post(self, request,user_id,channel_id):
        data = request.data.dict()
        data['user_id'] = user_id
        data['channel_id'] = channel_id

        serializer = AudioSerializer(data = data)

        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response({"data":serializer.data})

class  PodcastView(APIView):
    def get(self, request, user_id,channel_id,id):
        audio = Audio.objects.get(id=id)
        serializer = AudioSerializer(audio)
        
        return Response(serializer.data) 
    
    def put(self, request, user_id,channel_id,id):
        audio = Audio.objects.get(id=id)
        data = request.data.dict()
        data['user_id'] = user_id
        data['channel_id'] = channel_id

        serializer = AudioSerializer(audio, data=data)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response(serializer.data)

    def delete(self, request, user_id,channel_id,id):
        audio = Audio.objects.get(id=id)

        audio.delete()
        return Response("deleted")
        

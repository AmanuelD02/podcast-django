import os
from pathlib import Path
import mimetypes
from django.http.response import HttpResponse


from django.shortcuts import render
from rest_framework import permissions
from audios.models import Audio
from rest_framework import serializers
from rest_framework.views import APIView
from django.shortcuts import get_object_or_404
from rest_framework.response import Response

from audios.serializers import AudioSerializer
from rest_framework.permissions import AllowAny, OperandHolder

# Create your views here.
class PostPodcastView(APIView):
    def post(self, request,user_id,channel_id):
        data = request.data.dict()
        data['user_id'] = user_id
        data['channel_id'] = channel_id

        serializer = AudioSerializer(data = data)

        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response(serializer.data)

class PodcastView(APIView):
    def get(self, request, user_id,channel_id,id):
        audio = get_object_or_404(Audio, pk=id)
        serializer = AudioSerializer(audio)
        
        return Response(serializer.data) 
    
    def put(self, request, user_id,channel_id,id):
        audio = get_object_or_404(Audio, pk=id)
        data = request.data.dict()
        data['user_id'] = user_id
        data['channel_id'] = channel_id

        serializer = AudioSerializer(audio, data=data)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response(serializer.data)

    def delete(self, request, user_id,channel_id,id):
        audio = get_object_or_404(Audio, pk=id)

        audio.delete()
        return Response("deleted")
        


class DownloadPodcastView(APIView):
    permission_classes = [AllowAny, ]
    def get(self, request, id):
        
        audio = get_object_or_404(Audio, pk=id)

        filename = audio.path.name
        path = audio.path.path
        filepath = open(path, 'rb')
        mime_type, _ = mimetypes.guess_type(path)
        # Set the return value of the HttpResponse
        response = HttpResponse(filepath, content_type=mime_type)
        # Set the HTTP header for sending to browser
        response['Content-Disposition'] = "attachment; filename=%s" % filename
        # Return the response value
        return response

class PodcastsView(APIView):
    def get(self, request,channel_id):
        audios = Audio.objects(channel_id=channel_id)
        serializer = AudioSerializer(audios, many=True)

        return Response(serializer.data)



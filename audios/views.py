import os
from pathlib import Path
import mimetypes
from random import Random
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

def get_random_pics(serializer):
    for i in range(len(serializer.data)):
        serializer.data[i]["poster"] = Random().choice(
            ["/media/media/music1.jfif",
            "/media/media/music2.jfif",
            "/media/media/music3.png",
            "/media/media/music4.png",
            "/media/media/music5.jfif",
            "/media/media/music6.jfif",
            "/media/media/music7.jfif",
            "/media/media/music8.jfif",
            "/media/media/music9.jfif",])

# Create your views here.
class PostPodcastView(APIView):
    def post(self, request):
        data = request.data
        serializer = AudioSerializer(data = data)

        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response(serializer.data)

class PodcastView(APIView):
    def get(self, request,id):
        audio = get_object_or_404(Audio, pk=id)
        serializer = AudioSerializer(audio)
        
        return Response(serializer.data) 
    
    def put(self, request,id):
        audio = get_object_or_404(Audio, pk=id)
        data = request.data

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
        audios = Audio.objects.filter(channel_id=channel_id)
        serializer = AudioSerializer(audios, many=True)
        get_random_pics(serializer)
        return Response(serializer.data)


class GetRecentlyView(APIView):
    def get(self,request):
        audio = Random().choices(Audio.objects.all(), k=4)
        
        serializer = AudioSerializer(audio, many=True)
        get_random_pics(serializer)
        return Response(serializer.data)


from django.shortcuts import render
from ratings.models import Rating
from rest_framework import serializers
from rest_framework.views import APIView
from django.shortcuts import get_object_or_404
from rest_framework.response import Response

from ratings.serializers import RatingSerializer
# Create your views here.
class PostRatingView(APIView):
    def post(self, request):
        data = request.data.dict()

        serializer = RatingSerializer(data = data)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response({"data":serializer.data})

class RatingView(APIView):
    def get(self, request, id):
        rating = get_object_or_404(Rating, pk=id)
        serializer = RatingSerializer(rating)

        return Response(serializer.data)
    
    def put(self, request, id):
        rating = get_object_or_404(Rating, pk=id)
        data = request.data.dict()

        serializer = RatingSerializer(rating, data = data)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response(serializer.data)

    def delete(self, request, id):
        rating = get_object_or_404(Rating, pk=id)

        rating.delete()
        return Response("deleted")

class RatingsView(APIView):
    def get(self, request, channel_id):
        ratings = Rating.objects.filter(channel_id=channel_id)
        serializer = RatingSerializer(ratings, many=True)

        return Response(serializer.data)
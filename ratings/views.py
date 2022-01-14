from django.shortcuts import render
from ratings.models import Rating
from rest_framework import status
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

        return Response(serializer.data)

class RatingView(APIView):
    def get(self, request, channel_id, user_id):
        rating = Rating.objects.filter(channel_id=channel_id).filter(user_id=user_id).first()
        serializer = RatingSerializer(rating)

        return Response(serializer.data)
    
    def put(self, request, channel_id, user_id):
        rating = Rating.objects.filter(channel_id=channel_id).filter(user_id=user_id).first()
        data = request.data.dict()

        serializer = RatingSerializer(rating, data = data)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response(serializer.data)

    def delete(self, request, channel_id, user_id):
        rating = Rating.objects.filter(channel_id=channel_id).filter(user_id=user_id).first()

        rating.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
        

class RatingsView(APIView):
    def get(self, request, channel_id):
        ratings = Rating.objects.filter(channel_id=channel_id)
        serializer = RatingSerializer(ratings, many=True)

        return Response(serializer.data)

class IsRatedView(APIView):
    def get(self, request,channel_id,user_id):
        isRated = Rating.objects.filter(channel_id=channel_id).filter(user_id=user_id).first()
         
        if isRated:
            return Response(True)
        
        return Response(False)

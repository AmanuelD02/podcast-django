from django.shortcuts import render
from rest_framework import serializers
from rest_framework.views import APIView
from django.shortcuts import get_object_or_404
from rest_framework.response import Response

from ratings.serializers import RatingSerializer
# Create your views here.
class RatingView(APIView):
    def post(self, request, channel_id):
        data = request.data.dict()
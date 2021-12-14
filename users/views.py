from django.shortcuts import render
from rest_framework.views import APIView
from django.shortcuts import get_object_or_404
from rest_framework.response import Response

from .models import User, Subscribe
# Create your views here.


class RegisterView(APIView):
    pass




from django.contrib.auth import authenticate
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework import serializers
import django.contrib.auth.password_validation as validators


class Utils:
    @staticmethod
    def encode_token(user):
        payload = {
            'id': user.id,
        }
        token = RefreshToken.for_user(user)
        token.payload['TOKEN_TYPE_CLAIM'] = 'access'

        return {
            'refresh': str(token),
            'access': str(token.access_token),
        }
    @staticmethod
    def authenticate_user(validated_data):
        from .models import User
        email = validated_data['email']
        password = validated_data['password']
        
        user = User.objects.filter(email=email).first()
        if user and authenticate(username = email, password= password):
            return user
            
        
        raise serializers.ValidationError("Invalid email/password. Please try again!")



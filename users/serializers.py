from rest_framework import fields, serializers
from .models import User

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id','email', 'password','first_name','last_name', 'profile_pic','username']
        extra_kwargs = {'password': {'write_only': True}}
        read_only_fields = ['id']
    
    def create(self, validated_data):
        if validated_data.get('profile_pic'):
            user = User(email= validated_data['email'], first_name=validated_data['first_name'], last_name = validated_data['last_name'], profile_pic= validated_data['profile_pic'], username = validated_data['username'] )
        else:
            user = User(email= validated_data['email'], first_name=validated_data['first_name'], last_name = validated_data['last_name'], username = validated_data['username'] )

        user.set_password(validated_data['password'])
        user.save()
        return user


class LoginSerializer(serializers.Serializer):
    password = serializers.CharField(required=True, write_only=True)
    email = serializers.EmailField(required=True)

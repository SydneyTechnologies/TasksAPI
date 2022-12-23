from rest_framework import serializers
from . models import CustomUser

class CustomUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ["email", "username", "password"]
        extra_kwargs = {'password': {'write_only': True, 'style':{'input_type':'password'}}}
    
    # lets take create functionality and update it here
    def create(self, validated_data):
        username = validated_data["username"]
        email = validated_data["email"]
        password = validated_data["password"]
        user = CustomUser.objects.create_user(email=email, username=username, password=password)
        return user


class LoginSerializer(serializers.Serializer):
    username = serializers.CharField(required=True)
    password = password = serializers.CharField(
        write_only=True,
        required=True,
        style={'input_type': 'password', 'placeholder': 'Password'}
    )
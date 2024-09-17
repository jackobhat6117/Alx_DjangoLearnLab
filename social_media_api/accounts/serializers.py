from rest_framework import serializers
from .models import CustomUser
from rest_framework.authtoken.models import Token
from django.contrib.auth import authenticate
from django.contrib.auth import get_user_model



class RegisterSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = CustomUser
        fields = ['username', 'password', 'email', 'bio', 'profile_picture']
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = get_user_model.objects.create_user(
            username = validated_data['username'],
            password = validated_data['password'],
            email = validated_data.get('email', None),
            bio = validated_data.get('bio', ''),
            profile_picture = validated_data.get('profile_picture', None)
        )
        Token.objects.create(user = user)
        return user 
    
class LoginSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField()


    def validate(self, data):
        user = authenticate(**data)
        if user:
            token, created = Token.objects.get_or_create(user = user)
            return {'token', token.key}
        raise serializers.ValidationError("Invalid credentials")



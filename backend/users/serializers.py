from rest_framework import serializers
from .models import CustomUser

class userRegisterationSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = CustomUser
        fields = ['email', 'username', 'firstName', 'lastName', 'password', 'isStudent']

    def create(self, validated_data):
        user = CustomUser.objects.create_user(
            email=validated_data['email'],
            username=validated_data['username'],
            firstName=validated_data['firstName'],
            lastName=validated_data['lastName'],
            password=validated_data['password'],
            isStudent=validated_data['isStudent'] 
        )
        return user
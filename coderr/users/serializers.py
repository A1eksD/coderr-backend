from rest_framework import serializers
from users.models import CustomUser
from django.contrib.auth import get_user_model



class UserSerializer(serializers.ModelSerializer):
    repeated_password = serializers.CharField(write_only=True)
    
    class Meta:
        model = CustomUser
        fields = ['username', 'email', 'password', 'repeated_password', 'type']
    
    def validate(self, data): 
        if data['password'] != data['repeated_password']:
            raise serializers.ValidationError("The passwords do not match.")
        return data
    
    def create(self,validated_data):
        validated_data.pop('repeated_password')

        user = get_user_model().objects.create_user(
            username=validated_data['username'],
            email=validated_data['email'],
            password=validated_data['password'],
        )
        user.is_active = True
        user.save()
        return user
    
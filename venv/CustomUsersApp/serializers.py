from rest_framework import serializers
from dj_rest_auth.registration.serializers import RegisterSerializer
from .models import CustomUser

# Serializer for CustomUser model
class CustomUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ['id', 'username', 'email', 'role']

class CustomRegisterSerializer(RegisterSerializer):
    role = serializers.CharField(max_length=20)

    def get_cleaned_data(self):
        data = super().get_cleaned_data()
        data['role'] = self.validated_data.get('role') 
        return data

    def create(self, validated_data):
        user = super().create(validated_data)
        user.role = validated_data.get('role') 
        user.save() 
        return user

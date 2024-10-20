from rest_framework import serializers
from dj_rest_auth.registration.serializers import RegisterSerializer
from .models import CustomUser

class CustomUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ['id', 'username', 'email', 'role']

class CustomRegisterSerializer(RegisterSerializer):
    role = serializers.ChoiceField(choices=CustomUser.ROLE_CHOICES)

    def get_cleaned_data(self):
        data = super().get_cleaned_data()
        data['role'] = self.validated_data.get('role', 'football_player')
        return data

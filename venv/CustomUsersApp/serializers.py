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
        data['role'] = self.validated_data.get('role')  # Ensure to get the role from validated data
        return data

    def create(self, validated_data):
        user = super().create(validated_data)  # Call the parent create method
        user.role = validated_data.get('role')  # Set the role from validated data
        user.save()  # Save the user to ensure the role is saved
        return user

from django.shortcuts import render
from dj_rest_auth.registration.views import RegisterView
from rest_framework.response import Response
from rest_framework import status
from CustomUsersApp.serializers import CustomRegisterSerializer
from rest_framework.permissions import AllowAny
from dj_rest_auth.views import PasswordResetView
from allauth.account.models import EmailConfirmation, EmailConfirmationHMAC
from rest_framework.views import APIView
from django.http import Http404
# Create your views here.


class CustomRegisterView(RegisterView):
    serializer_class = CustomRegisterSerializer
    permission_classes = [AllowAny]

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response({
            'user': serializer.data,
            'message': 'User registered successfully.'
        }, status=status.HTTP_201_CREATED, headers=headers)


class CustomPasswordResetView(PasswordResetView):
    def post(self, request, *args, **kwargs):
        response = super().post(request, *args, **kwargs)
        return Response({'message': 'Password reset email sent.'})




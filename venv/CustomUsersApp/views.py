from dj_rest_auth.registration.views import RegisterView
from rest_framework.permissions import AllowAny
from rest_framework import generics
from .models import CustomUser
from .serializers import CustomRegisterSerializer, CustomUserSerializer

# Custom Register View
class CustomRegisterView(RegisterView):
    serializer_class = CustomRegisterSerializer
    permission_classes = [AllowAny]

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)

        # Add a message to the response to confirm successful registration
        return Response({
            'message': 'Registration successful!',
            'username': user.username,
            'email': user.email,
            'role': user.role,
        }, status=status.HTTP_201_CREATED, headers=headers)


# If you want to add a view for listing users or fetching user details
class UserListView(generics.ListAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = CustomUserSerializer
    permission_classes = [AllowAny]  # Adjust permissions as needed

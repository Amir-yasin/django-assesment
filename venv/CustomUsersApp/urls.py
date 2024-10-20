from django.urls import path
from dj_rest_auth.registration.views import RegisterView
from dj_rest_auth.views import PasswordResetView, LoginView
from allauth.socialaccount.providers.google.views import GoogleOAuth2Adapter
from allauth.socialaccount.providers.facebook.views import FacebookOAuth2Adapter
from dj_rest_auth.registration.views import SocialLoginView

# Define custom views for Google and Facebook login
class GoogleLogin(SocialLoginView):
    adapter_class = GoogleOAuth2Adapter

class FacebookLogin(SocialLoginView):
    adapter_class = FacebookOAuth2Adapter

# Initialize urlpatterns
urlpatterns = [
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', LoginView.as_view(), name='login'),
    path('password-reset/', PasswordResetView.as_view(), name='password_reset'),
    path('social/google/', GoogleLogin.as_view(), name='google_login'),
    path('social/facebook/', FacebookLogin.as_view(), name='facebook_login'),
]


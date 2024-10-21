from django.urls import path
from dj_rest_auth.registration.views import RegisterView
from dj_rest_auth.views import PasswordResetView, LoginView
from allauth.socialaccount.providers.google.views import GoogleOAuth2Adapter
from allauth.socialaccount.providers.facebook.views import FacebookOAuth2Adapter
from dj_rest_auth.registration.views import SocialLoginView
from django.contrib.auth import views as auth_views




# Custom social login views
class GoogleLogin(SocialLoginView):
    adapter_class = GoogleOAuth2Adapter

class FacebookLogin(SocialLoginView):
    adapter_class = FacebookOAuth2Adapter

# All paths combined into one `urlpatterns`
urlpatterns = [
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', LoginView.as_view(), name='login'),
    path('password-reset/', PasswordResetView.as_view(), name='password_reset'),
    path('social/google/', GoogleLogin.as_view(), name='google_login'),
    path('social/facebook/', FacebookLogin.as_view(), name='facebook_login'),
    path('password-reset-confirm/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(), name='password_reset_confirm'),

]

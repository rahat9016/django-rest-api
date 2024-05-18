from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from django.urls import path
from .views import SignUpView
urlpatterns = [
    path('signup/', SignUpView.as_view(), name='Signup'),
    path('login/', TokenObtainPairView.as_view(), name="token_obtain"),
    path('refresh/', TokenRefreshView.as_view(), name='token_refresh')
]

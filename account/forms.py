from django.contrib.auth.forms import UserCreationForm
from . models import Users
from rest_framework.serializers import ModelSerializer

class SignupSerializer(ModelSerializer):
    class Meta:
        model = Users
        fields = ['email', 'name', 'password1', 'password2']
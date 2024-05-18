from .models import Users
from rest_framework.serializers import ModelSerializer,SerializerMethodField

class SignupSerializer(ModelSerializer):
   
    class Meta:
        model = Users
        fields = ['email', 'name', 'password1', 'password2']
        extra_kwargs = { 'password1': { 'write_only': True},
                        'password2': { 'write_only': True}}
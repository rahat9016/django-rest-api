from django.http import JsonResponse
from rest_framework.decorators import api_view, authentication_classes, permission_classes
from rest_framework.generics import ListCreateAPIView
from rest_framework.views import APIView
from .serializers import SignupSerializer
from .models import Users
from rest_framework.response import Response
# @api_view(['POST'])
# @authentication_classes([])
# @permission_classes([])
# def signup(request):
    
    
#     return JsonResponse({'status': message})

class SignUpView(APIView):
    def post(self,request):
        # email=request.data['email']
        # name=request.data['name']
        # password1=request.data['password1']
        # password2=request.data['password2']
        
        # user=Users()
        # user.email=email
        # user.name=name
        # user.password1=password1
        # user.password2=password2
        # user.save()
        serializer=SignupSerializer(data=request.data)
        if(serializer.is_valid()):
            serializer.save()
            return Response({"message":"register successful"})
        
        return Response({"message":serializer.errors})
    
    def get(self,request):
        user=Users.objects.all()
        serializer=SignupSerializer(user,many=True)
        return Response({"data":serializer.data})
        

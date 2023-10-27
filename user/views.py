from django.shortcuts import render
from rest_framework.decorators import api_view, permission_classes
from django.contrib.auth import authenticate
from rest_framework.response import Response
from rest_framework.authtoken.models import Token
from rest_framework.permissions import AllowAny
from .serializers import *
from django.contrib.auth.hashers import make_password

# Create your views here.

@api_view(['POST'])
@permission_classes([AllowAny])
def login(request):
    email = request.data.get('email')
    password = request.data.get('password')
    user = authenticate(username = email, password = password)
    if user == None:
        return Response('Invalid email or password!')
    else:
        token,_ = Token.objects.get_or_create(user = user)
        return Response({'token': token.key})
    
@api_view(['POST'])
@permission_classes([AllowAny])
def register(request):
    password = request.data.get('password')
    request.data['password'] = make_password(password)
    serializer = UserSerializer(data = request.data)
    if serializer.is_valid():
        serializer.save()
        return Response('user created!')
    else:
        return Response(serializer.errors)

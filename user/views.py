from django.shortcuts import render
from rest_framework.decorators import api_view, permission_classes
from django.contrib.auth import authenticate
from rest_framework.response import Response
from rest_framework.authtoken.models import Token
from rest_framework.permissions import AllowAny
from .serializers import *
from django.contrib.auth.hashers import make_password
from django.contrib.auth.models import Group
from rest_framework.generics import GenericAPIView
from django_filters.rest_framework import DjangoFilterBackend 
from rest_framework import filters

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
    # group_id = request.data.get('role')
    # group = Group.objects.get(id = group_id)
    password = request.data.get('password')
    request.data['password'] = make_password(password)
    serializer = UserSerializer(data = request.data)
    if serializer.is_valid():
        serializer.save()
        return Response('user created!')
    else:
        return Response(serializer.errors)
    

class UserApi(GenericAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    filter_backends = [DjangoFilterBackend, filters.SearchFilter]
    filterset_fields = ['groups', 'email']
    search_fields = ['groups', 'email'] 

    def get(self, request):
        queryset = self.get_queryset()
        filter_queryset = self.filter_queryset(queryset)
        serializer = self.serializer_class(filter_queryset, many = True)
        return Response(serializer.data)

class UserIdApiView(GenericAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    def get(self, request, pk):
        try:
            queryset = User.objects.get(id=pk)
        except:
            return Response("Not found")
        serializer = self.serializer_class(queryset)
        return Response(serializer.data)
'''
    def put(self, request, pk):
        queryset = User.objects.get(id=pk)
        serializer =self.serializer_class(queryset, data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response('data updated')
        else:
            return Response (serializer.errors)
        
    def delete(self, request, pk ):
        queryset = User.objects.get(id = pk)
        queryset.delete()
        return Response('data deleted')

        '''
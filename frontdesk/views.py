from django.shortcuts import render
from rest_framework.decorators import api_view
from .models import *
from .serializers import *
from rest_framework.response import Response
from rest_framework.generics import GenericAPIView
from core.permissions import CustomModelPermission
from django.contrib.auth.models import Group 
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters

# Create your views here.
'''
def home(request): # For template based django project
    return render()

# Request methods = 'GET', 'Post', 'Put', 'Patch', 'Delete'
@api_view(['GET'])
def guestInfoApiView(request):
    queryset = GuestInfo.objects.all()
    serializer = GuestInfoSerializer(queryset, many=True)
    return Response(serializer.data)
'''

class GuestInfoApiView(GenericAPIView):
    queryset = GuestInfo.objects.all()
    serializer_class = GuestInfoSerializer
    permission_classes = [CustomModelPermission]
    filter_backends = [DjangoFilterBackend, filters.SearchFilter] #can be seprated
    #filterset_fields = ['category', 'in_stock'] #
    search_fields = ['f_name', 'l_name'] #
    filterset_fields = ['f_name']

    def get(self, request):
        queryset = self.get_queryset()
        filter_queryset = self.filter_queryset(queryset)
        serializer = self.serializer_class(filter_queryset, many=True)
        return Response(serializer.data)
    
    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response('data created')
        else:
            return Response(serializer.errors)

class GuestInfoIdApiView(GenericAPIView):
    queryset = GuestInfo.objects.all()
    serializer_class = GuestInfoSerializer

    def get(self, request, pk):
        try:
            queryset = GuestInfo.objects.get(id=pk)
        except:
            return Response("Not found")
        serializer = self.serializer_class(queryset)
        return Response(serializer.data)
    
    def put(self, request, pk):
        queryset = GuestInfo.objects.get(id=pk)
        serializer =self.serializer_class(queryset, data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response('data updated')
        else:
            return Response (serializer.errors)
        
    def delete(self, request, pk ):
        queryset = GuestInfo.objects.get(id = pk)
        queryset.delete()
        return Response('data deleted')
    
class GroupApiView(GenericAPIView):
    queryset = Group.objects.all()
    serializer_class = GroupSerializer

    def get(self, request):
        queryset = self.get_queryset()
        serializer = self.serializer_class(queryset, many = True)
        return Response(serializer.data)

from django.shortcuts import render
from rest_framework.decorators import api_view
from .models import *
from .serializers import *
from rest_framework.response import Response
from rest_framework.generics import GenericAPIView

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

    def get(self, request):
        queryset = self.get_queryset()
        serializer = self.serializer_class(queryset, many=True)
        return Response(serializer.data)
    
    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response('data created')
        else:
            return Response(serializer.errors)


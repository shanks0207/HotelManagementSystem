from rest_framework import serializers
from .models import *

class GuestInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = GuestInfo 
        fields = '__all__'

class RoomTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = RoomType
        fields = '__all__'

class RoomSerializer(serializers.ModelSerializer):
    class Meta:
        model = Room
        fields = '__all__'

class GuestRoomSerializer(serializers.ModelSerializer):
    class Meta:
        model = GuestRoom
        fields = '__all__'
        
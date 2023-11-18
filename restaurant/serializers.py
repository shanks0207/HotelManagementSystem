from rest_framework import serializers
from .models import *
from django.contrib.auth.models import Group

class MenuSerializer(serializers.ModelSerializer):
    class Meta:
        model = Menu 
        fields = '__all__'

class FoodSerializer(serializers.ModelSerializer):
    class Meta:
        model = Food
        fields = '__all__'



class GroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = Group
        fields = ['id', 'name']
        
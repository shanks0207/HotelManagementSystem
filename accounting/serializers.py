from rest_framework import serializers
from .models import *
from django.contrib.auth.models import Group

class BillSerializer(serializers.ModelSerializer):
    class Meta:
        model = Bill 
        fields = '__all__'

class PaymentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Payment
        fields = '__all__'


class GroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = Group
        fields = ['id', 'name']
        
from django.db import models
from django.db.models import fields
from rest_framework import serializers
from rest_framework.fields import ReadOnlyField
from .models import Restaurant, Pizza

class RestaurantSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(read_only=True)
    
    class Meta: 
        model = Restaurant
        fields = '__all__'

class PizzaSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(read_only=True)
    
    class Meta: 
        model = Pizza
        fields = '__all__'

    
from rest_framework import serializers
from .models import BronModel

class BronSerializer(serializers.ModelSerializer):
    model = BronModel
    fields = ('__all__')

class FreeTimeSerializer(serializers.ModelSerializer):
    model = BronModel
    fields = ('free_time',)
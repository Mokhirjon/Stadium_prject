from rest_framework import serializers
from .models import StadiumModel


class StadiumSerializer(serializers.ModelSerializer):
    model = StadiumModel
    fields = ('__all__')
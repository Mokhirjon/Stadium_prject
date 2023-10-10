from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from .models import StadiumModel
from rest_framework import generics
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from .serializers import *
from config.permissions import AdminPermissionClass, OwnerPermissionClass, BronerPermissionClass
from django_filters.rest_framework import DjangoFilterBackend

class StadiumListAPIView(generics.ListAPIView):
    queryset = StadiumModel.objects.all()
    serializer_class = StadiumSerializer
    permission_classes = (IsAuthenticatedOrReadOnly, AdminPermissionClass | OwnerPermissionClass | BronerPermissionClass)
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['stadium_name', 'stadium_address']
class StadiumCreateAPIView(generics.CreateAPIView):
    queryset = StadiumModel.objects.all()
    serializer_class = StadiumSerializer
    permission_classes = (IsAuthenticatedOrReadOnly, AdminPermissionClass | OwnerPermissionClass)

class StadiumUpdateAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = StadiumModel.objects.all()
    serializer_class = StadiumSerializer
    permission_classes = (IsAuthenticatedOrReadOnly, AdminPermissionClass | OwnerPermissionClass)
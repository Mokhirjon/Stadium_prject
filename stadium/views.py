from django.shortcuts import render
from .models import StadiumModel
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from .serializers import *
from config.permissions import AdminPermissionClass, OwnerPermissionClass, BronerPermissionClass

class StadiumListAPIView(generics.ListAPIView):
    queryset = StadiumModel.objects.all()
    serializer_class = StadiumSerializer
    permission_classes = (IsAuthenticated, AdminPermissionClass | OwnerPermissionClass | BronerPermissionClass)

class StadiumCreateAPIView(generics.CreateAPIView):
    queryset = StadiumModel.objects.all()
    serializer_class = StadiumSerializer
    permission_classes = (IsAuthenticated, AdminPermissionClass | OwnerPermissionClass)

class StadiumUpdateAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = StadiumModel.objects.all()
    serializer_class = StadiumSerializer
    permission_classes = (IsAuthenticated, AdminPermissionClass | OwnerPermissionClass)


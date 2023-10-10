from django.shortcuts import render

# Create your views here.

from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from .models import BronModel
from .serializers import BronSerializer
from config.permissions import AdminPermissionClass, OwnerPermissionClass, BronerPermissionClass

# Category
class BronStadiumListAPIView(generics.ListAPIView):
    queryset = BronModel.objects.all()
    serializer_class = BronSerializer
    permission_classes = (IsAuthenticated, AdminPermissionClass | OwnerPermissionClass | BronerPermissionClass)

class BronStadiumCreateAPIView(generics.CreateAPIView):
    queryset = BronModel.objects.all()
    serializer_class = BronSerializer
    permission_classes = (IsAuthenticated, AdminPermissionClass | OwnerPermissionClass)

class BronStadiumUpdateAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = BronModel.objects.all()
    serializer_class = BronSerializer
    permission_classes = (IsAuthenticated, AdminPermissionClass | OwnerPermissionClass)



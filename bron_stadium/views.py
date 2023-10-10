from django.shortcuts import render

# Create your views here.
from rest_framework import generics
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from .models import BronModel
from .serializers import BronSerializer
from config.permissions import AdminPermissionClass, OwnerPermissionClass, BronerPermissionClass
from rest_framework import filters

# Category
class BronStadiumListAPIView(generics.ListAPIView):
    queryset = BronModel.objects.all()
    serializer_class = BronSerializer
    permission_classes = (IsAuthenticatedOrReadOnly, AdminPermissionClass | OwnerPermissionClass | BronerPermissionClass)
    filter_backends = [filters.SearchFilter]
    search_fields = ['bron_name', 'free_time']
class BronStadiumCreateAPIView(generics.CreateAPIView):
    queryset = BronModel.objects.all()
    serializer_class = BronSerializer
    permission_classes = (IsAuthenticatedOrReadOnly, AdminPermissionClass | OwnerPermissionClass)

class BronStadiumUpdateAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = BronModel.objects.all()
    serializer_class = BronSerializer
    permission_classes = (IsAuthenticatedOrReadOnly, AdminPermissionClass | OwnerPermissionClass)
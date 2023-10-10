from django.urls import path
from .views import *

urlpatterns = [
    path('stadium/all/', StadiumListAPIView.as_view()),
    path('stadium/create/', StadiumCreateAPIView.as_view()),
    path('update_stadium/<int:pk>/', StadiumUpdateAPIView.as_view()),
]
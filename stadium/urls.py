from django.urls import path
from .views import *

urlpatterns = [
    path('all/', StadiumListAPIView.as_view()),
    path('create/', StadiumCreateAPIView.as_view()),
    path('update_stadium/<int:pk>/', StadiumUpdateAPIView.as_view()),
]
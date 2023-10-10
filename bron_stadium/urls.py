from django.urls import path
from .views import BronStadiumListAPIView, BronStadiumCreateAPIView, BronStadiumUpdateAPIView

urlpatterns = [
    path('bron_stadium/all/', BronStadiumListAPIView.as_view()),
    path('bron_stadium/create/', BronStadiumCreateAPIView.as_view()),
    path('update_bron_stadium/<int:pk>/', BronStadiumUpdateAPIView.as_view())
]
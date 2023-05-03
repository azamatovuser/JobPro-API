from django.urls import path
from .views import ContactPostAPIView, SubscribePostAPIView


urlpatterns = [
    path('contact/', ContactPostAPIView.as_view()),
    path('subscribe/', SubscribePostAPIView.as_view()),
]
from django.urls import path
from .views import AccountListAPIView


urlpatterns = [
    path('list/', AccountListAPIView.as_view()),
]
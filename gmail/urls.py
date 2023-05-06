from django.urls import path
from .views import GmailSendAPIView


urlpatterns = [
    path('', GmailSendAPIView.as_view()),
]
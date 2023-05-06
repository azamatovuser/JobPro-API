import requests
from django.core.mail import send_mail
from django.conf import settings
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Gmail
from main.models import Subscribe


class GmailSendAPIView(APIView):

    def post(self, request):
        message = request.data.get('message')
        print(message)
        send_mail(
            'This is JobPro company',
            message,
            'settings.EMAIL_HOST_USER',
            [i.email for i in Subscribe.objects.all()],
            fail_silently=False
        )
        instance = Gmail.objects.create(message=message)
        return Response('Message was sent successfully!')
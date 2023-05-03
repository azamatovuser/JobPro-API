from rest_framework import generics
from .models import Contact, Subscribe
from .serializers import ContactSerializer, SubscribeSerializer



class ContactPostAPIView(generics.CreateAPIView):
    #  http://127.0.0.1:8000/main/contact/
    queryset = Contact.objects.all()
    serializer_class = ContactSerializer



class SubscribePostAPIView(generics.CreateAPIView):
    #  http://127.0.0.1:8000/main/subscribe/
    queryset = Subscribe.objects.all()
    serializer_class = SubscribeSerializer
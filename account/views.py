from rest_framework import generics
from .serializers import AccountSerializer
from .models import Account


class AccountListAPIView(generics.ListAPIView):
    #  http://127.0.0.1:8000/account/list/
    queryset = Account.objects.all()
    serializer_class = AccountSerializer

    def get_queryset(self):
        qs = super().get_queryset()
        if qs:
            return qs.filter(type=1)
        return qs


class AccountRUDAPIView(generics.RetrieveUpdateDestroyAPIView):
    #  http://127.0.0.1:8000/account/detail/<int:account_id>/
    queryset = Account.objects.all()
    serializer_class = AccountSerializer
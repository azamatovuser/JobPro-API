from rest_framework import serializers
from .models import Account, City, Country


class CountrySerializer(serializers.ModelSerializer):
    class Meta:
        model = Country
        fields = ['id', 'title']


class CitySerializer(serializers.ModelSerializer):
    country = CountrySerializer(read_only=True)
    class Meta:
        model = City
        fields = ['id', 'country', 'title']


class AccountSerializer(serializers.ModelSerializer):
    city = CitySerializer(read_only=True)
    class Meta:
        model = Account
        fields = ['id', 'username', 'first_name', 'last_name', 'avatar', 'bio', 'type', 'city']
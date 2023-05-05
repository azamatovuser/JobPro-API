from rest_framework import serializers
from .models import Job, Company, Position, Type, Category, Wishlist
from account.serializers import AccountSerializer, CitySerializer


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'title']


class TypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Type
        fields = ['id', 'title']


class CompanySerializer(serializers.ModelSerializer):
    class Meta:
        model = Company
        fields = ['id', 'title']


class JobSerializer(serializers.ModelSerializer):
    types = TypeSerializer(read_only=True, many=True)
    company = CompanySerializer(read_only=True)
    author = AccountSerializer(read_only=True)
    class Meta:
        model = Job
        fields = ['id', 'author', 'title', 'position', 'types', 'company','salary']


class JobRetrieveSerializer(serializers.ModelSerializer):
    author = AccountSerializer(read_only=True)
    company = CompanySerializer(read_only=True)
    types = TypeSerializer(read_only=True, many=True)
    category = CategorySerializer(read_only=True)
    class Meta:
        model = Job
        fields = ['id', 'author', 'title', 'description', 'position', 'company', 'salary', 'types', 'category', 'is_active', 'created_date']


class JobPostSerializer(serializers.ModelSerializer):
    company = CompanySerializer()
    types = TypeSerializer(many=True)
    city = CitySerializer()
    class Meta:
        model = Job
        fields = ['id', 'salary', 'title', 'company','city', 'types', 'description']


    # def create(self, validated_data):
    #     request = self.context['request']
    #     company = request['company']
    #     print(company)


class WishlistSerializer(serializers.ModelSerializer):
    author = AccountSerializer(read_only=True)
    job = JobRetrieveSerializer(read_only=True,many=True)
    class Meta:
        model = Wishlist
        fields = ['id', 'author', 'job']
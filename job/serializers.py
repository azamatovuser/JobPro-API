from rest_framework import serializers
from .models import Job, Company, Position, Type, Category, Wishlist, ApplyJob
from account.serializers import AccountSerializer, CitySerializer
from rest_framework.exceptions import ValidationError


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
    company = CompanySerializer(read_only=True)
    types = TypeSerializer(read_only=True, many=True)
    class Meta:
        model = Job
        fields = ['id', 'author', 'title', 'description', 'salary', 'company', 'types']

    def validate(self, attrs):
        request = self.context['request']
        author = request.user
        if author.type == 1:
            raise ValidationError('You dont have permission')
        return attrs

    def create(self, validated_data):
        request = self.context['request']
        author = request.user
        instance = super().create(validated_data)
        instance.author = author
        instance.save()
        return instance


class WishlistSerializer(serializers.ModelSerializer):
    author = AccountSerializer()
    job = JobRetrieveSerializer()
    class Meta:
        model = Wishlist
        fields = ['id', 'author', 'job']


class ApplyJobSerializer(serializers.ModelSerializer):
    class Meta:
        model = ApplyJob
        fields = ['author', 'cv', 'message']
        extra_kwargs = {
            'author': {'required': False}
        }

    def validate(self, attrs):
        author = attrs.get('author')
        if not author.type == 1:
            raise ValidationError('You are not canditate!')
        return attrs


class ApplyJobGetSerializer(serializers.ModelSerializer):
    class Meta:
        model = ApplyJob
        fields = ['author', 'cv', 'message']
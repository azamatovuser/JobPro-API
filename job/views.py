from rest_framework import generics
from .serializers import JobSerializer, TypeSerializer, CategorySerializer, JobRetrieveSerializer
from .models import Job, Type, Category


class JobListAPIView(generics.ListAPIView):
    #  http://127.0.0.1:8000/job/list/
    queryset = Job.objects.all()
    serializer_class = JobSerializer


class JobRUDAPIView(generics.RetrieveUpdateDestroyAPIView):
    #  http://127.0.0.1:8000/job/detail/<int:job_id>/
    queryset = Job.objects.all()
    serializer_class = JobRetrieveSerializer


class TypeListAPIView(generics.ListAPIView):
    #  http://127.0.0.1:8000/job/type/list/
    queryset = Type.objects.all()
    serializer_class = TypeSerializer


class CategoryListAPIView(generics.ListAPIView):
    #  http://127.0.0.1:8000/job/category/list/
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
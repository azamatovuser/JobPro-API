from rest_framework import generics
from .serializers import JobSerializer, TypeSerializer, CategorySerializer, JobRetrieveSerializer, JobPostSerializer, WishlistSerializer
from .models import Job, Type, Category, Wishlist


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



class JobPostAPIView(generics.CreateAPIView):
    #  http://127.0.0.1:8000/job/post/
    queryset = Job.objects.all()
    serializer_class = JobPostSerializer



class WishlistListAPIView(generics.ListAPIView):
    #  http://127.0.0.1:8000/account/wishlist/
    queryset = Wishlist.objects.all()
    serializer_class = WishlistSerializer

    def get_queryset(self):
        qs = super().get_queryset()
        author_id = self.request.user.id
        return qs.filter(author_id=author_id)
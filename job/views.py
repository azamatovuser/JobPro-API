from rest_framework import generics
from .serializers import JobSerializer, TypeSerializer, CategorySerializer, JobRetrieveSerializer, \
    JobPostSerializer, WishlistSerializer, CitySerializer, ApplyJobSerializer, ApplyJobGetSerializer
from .models import Job, Type, Category, Wishlist, ApplyJob
from account.models import City
from rest_framework import permissions, serializers


class JobListAPIView(generics.ListAPIView):
    #  http://127.0.0.1:8000/job/list/
    queryset = Job.objects.all()
    serializer_class = JobSerializer

    def get_queryset(self):
        qs = super().get_queryset()
        search = self.request.GET.get('search')
        cat = self.request.GET.get('cat')
        location = self.request.GET.get('location')
        search_condition = Q()
        cat_condition = Q()
        location_condition = Q()
        if search:
            search_condition = Q(title__icontains=q)
        if cat:
            cat_condition = Q(category__title__exact=cat)
        if location:
            location_condition = Q(city__title__icontains=location)
        qs = qs.filter(search_condition, location_condition, cat_condition)
        return qs


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


class CityListAPIView(generics.ListAPIView):
    #  http://127.0.0.1:8000/job/city/list/
    queryset = City.objects.all()
    serializer_class = CitySerializer



class JobPostAPIView(generics.CreateAPIView):
    #  http://127.0.0.1:8000/job/post/
    queryset = Job.objects.all()
    serializer_class = JobPostSerializer
    permission_classes = [permissions.IsAuthenticated]



class WishlistListAPIView(generics.ListAPIView):
    #  http://127.0.0.1:8000/account/wishlist/
    queryset = Wishlist.objects.all()
    serializer_class = WishlistSerializer

    def get_queryset(self):
        qs = super().get_queryset()
        author_id = self.request.user.id
        return qs.filter(author_id=author_id)


class ApplyJobListCreateAPIView(generics.ListCreateAPIView):
    queryset = ApplyJob.objects.all()
    serializer_class = ApplyJobSerializer


class ApplyJobHRListAPIView(generics.ListAPIView):
    queryset = ApplyJob.objects.all()
    serializer_class = ApplyJobGetSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        qs = super().get_queryset()
        author = self.request.user
        if not author.type == 0:
            raise PermissionError('You are not HR!')
        job_id = self.kwargs.get('job_id')
        if author.type == '1':
            raise serializers.ValidationError("You aren't HR")
        return qs.filter(job_id=job_id)

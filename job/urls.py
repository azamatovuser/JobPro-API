from django.urls import path
from .views import JobListAPIView, TypeListAPIView, CategoryListAPIView, \
    JobRUDAPIView, JobPostAPIView, CityListAPIView, ApplyJobListCreateAPIView


urlpatterns = [
    path('list/', JobListAPIView.as_view()),
    path('detail/<int:pk>/', JobRUDAPIView.as_view()),
    path('post/', JobPostAPIView.as_view()),
    path('type/list/', TypeListAPIView.as_view()),
    path('category/list/', CategoryListAPIView.as_view()),
    path('city/list/', CityListAPIView.as_view()),
    path('applyjob/', ApplyJobListCreateAPIView.as_view()),
]
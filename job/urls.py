from django.urls import path
from .views import JobListAPIView, TypeListAPIView, CategoryListAPIView, JobRUDAPIView


urlpatterns = [
    path('list/', JobListAPIView.as_view()),
    path('detail/<int:pk>/', JobRUDAPIView.as_view()),
    path('type/list/', TypeListAPIView.as_view()),
    path('category/list/', CategoryListAPIView.as_view()),
]
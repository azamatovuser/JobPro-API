from django.urls import path
from .views import BlogListAPIView, BlogDetailAPIView


urlpatterns = [
    path('list/', BlogListAPIView.as_view()),
    path('detail/<int:pk>/', BlogDetailAPIView.as_view()),
]
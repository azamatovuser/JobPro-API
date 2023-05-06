from django.urls import path
from .views import BlogListAPIView, BlogDetailAPIView, CommentPostAPIView


urlpatterns = [
    path('list/', BlogListAPIView.as_view()),
    path('detail/<int:pk>/', BlogDetailAPIView.as_view()),
    path('comment_create/', CommentPostAPIView.as_view()),
]
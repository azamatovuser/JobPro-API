from rest_framework import generics
from .models import Blog, Comment, SubContent, Tag
from .serializers import BlogSerializer, BlogDetailSerializer, CommentSerializer


class BlogListAPIView(generics.ListAPIView):
    #  http://127.0.0.1:8000/blog/list/
    queryset = Blog.objects.all()
    serializer_class = BlogSerializer


class BlogDetailAPIView(generics.ListAPIView):
    #  http://127.0.0.1:8000/blog/detail/<int:blog_id>/
    queryset = Blog.objects.all()
    serializer_class = BlogDetailSerializer


class CommentPostAPIView(generics.CreateAPIView):
    #  http://127.0.0.1:8000/blog/comment_create/
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
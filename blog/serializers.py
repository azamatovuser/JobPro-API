from rest_framework import serializers
from .models import Blog, SubContent, Comment, Tag


class SubContentSerializer(serializers.ModelSerializer):
    class Meta:
        model = SubContent
        fields = '__all__'


class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ['author', 'blog', 'message', 'parent_comment', 'top_level_comment_id', 'created_date']


class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = ['id', 'title']


class BlogSerializer(serializers.ModelSerializer):
    comments = CommentSerializer(read_only=True, many=True)
    class Meta:
        model = Blog
        fields = ['id', 'author', 'title', 'description', 'image', 'comments', 'created_date']


class BlogDetailSerializer(serializers.ModelSerializer):
    subcontent = SubContentSerializer(read_only=True, many=True)
    tags = TagSerializer(read_only=True, many=True)
    comments = CommentSerializer(read_only=True, many=True)
    class Meta:
        model = Blog
        fields = ['id', 'author', 'title', 'description', 'image', 'subcontent','tags', 'comments', 'created_date']
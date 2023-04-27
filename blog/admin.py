from django.contrib import admin
from .models import Blog, Comment, SubContent, Tag


admin.site.register(Blog)
admin.site.register(Comment)
admin.site.register(SubContent)
admin.site.register(Tag)
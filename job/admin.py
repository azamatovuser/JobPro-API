from django.contrib import admin
from .models import Job, Position, Category


admin.site.register(Job)
admin.site.register(Position)
admin.site.register(Category)
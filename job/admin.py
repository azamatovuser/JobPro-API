from django.contrib import admin
from .models import Job, Position, Category, Type, Company


admin.site.register(Job)
admin.site.register(Position)
admin.site.register(Category)
admin.site.register(Type)
admin.site.register(Company)
from django.contrib import admin
from .models import Account, City, Country


admin.site.register(Account)
admin.site.register(City)
admin.site.register(Country)
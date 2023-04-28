from django.db import models
from django.contrib.auth.models import User


class Country(models.Model):
    title = models.CharField(max_length=221)


class City(models.Model):
    country = models.ForeignKey(Country, on_delete=models.CASCADE)
    title = models.CharField(max_length=221)


class Company(models.Model):
    title = models.CharField(max_length=221)

    def __str__(self):
        return self.title


class Account(models.Model):
    TYPE = (
        (0, 'HR'),
        (1, 'Candidate'),
        (2, 'Staff'),
    )
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    avatar = models.ImageField(upload_to='account_avatar/')
    type = models.IntegerField(choices=TYPE)
    bio = models.TextField()
    city = models.ForeignKey(City, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return self.user.username


class WorkHistory(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    location = models.ForeignKey(City, on_delete=models.CASCADE)
    start_date = models.DateField(auto_now_add=True)
    end_date = models.DateField(auto_now_add=True)
    is_current = models.BooleanField(default=True)
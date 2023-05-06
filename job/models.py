from django.db import models
from account.models import Account


class Position(models.Model):
    title = models.CharField(max_length=221)

    def __str__(self):
        return self.title


class Category(models.Model):
    title = models.CharField(max_length=221)

    def __str__(self):
        return self.title


class Type(models.Model):
    title = models.CharField(max_length=221)

    def __str__(self):
        return self.title


class Company(models.Model):
    title = models.CharField(max_length=221)

    def __str__(self):
        return self.title


class Job(models.Model):
    author = models.ForeignKey(Account, on_delete=models.CASCADE, related_name='author')
    title = models.CharField(max_length=221)
    description = models.TextField()
    position = models.ForeignKey(Position, on_delete=models.CASCADE, null=True, blank=True)
    company = models.ForeignKey(Company, on_delete=models.CASCADE, null=True, blank=True)
    salary = models.DecimalField(decimal_places=3, max_digits=4, null=True, blank=True)
    types = models.ManyToManyField(Type)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, null=True, blank=True)
    is_active = models.BooleanField(default=True)
    created_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title


class Wishlist(models.Model):
    author = models.ForeignKey(Account, on_delete=models.CASCADE)
    job = models.ForeignKey(Job, on_delete=models.CASCADE, related_name='job')


class ApplyJob(models.Model):
    author = models.ForeignKey(Account, on_delete=models.CASCADE)
    job = models.ForeignKey(Job, on_delete=models.CASCADE)
    cv = models.FileField(upload_to='cv_file/')
    message = models.TextField()
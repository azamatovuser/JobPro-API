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


class Job(models.Model):
    TYPES = (
        (0, "Full time"),
        (1, "Part time"),
        (2, "Freelance"),
        (3, "Internship"),
        (4, "Temporary"),
    )
    author = models.ForeignKey(Account, on_delete=models.CASCADE)
    title = models.CharField(max_length=221)
    description = models.TextField()
    position = models.ForeignKey(Position, on_delete=models.CASCADE)
    deadline = models.CharField(max_length=221)
    salary = models.DecimalField(decimal_places=3, max_digits=4, null=True, blank=True)
    types = models.IntegerField(choices=TYPES)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    created_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
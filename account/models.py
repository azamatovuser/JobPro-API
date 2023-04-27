from django.db import models
from django.contrib.auth.models import User


class Account(models.Model):
    POSITION = (
        (0, 'Employer'),
        (0, 'Worker'),
    )
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    avatar = models.ImageField(upload_to='account_avatar/')
    position = models.IntegerField(choices=POSITION)
    location = models.CharField(max_length=221)
    bio = models.TextField()
    company = models.CharField(max_length=221)

    def __str__(self):
        return self.user.username
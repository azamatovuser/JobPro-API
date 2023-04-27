from django.db import models


class Contact(models.Model):
    name = models.CharField(max_length=221)
    email = models.EmailField(unique=True)
    subject = models.CharField(max_length=221)
    message = models.TextField()

    def __str__(self):
        return f"{self.name}'s contact"


class Subscribe(models.Model):
    email = models.EmailField(unique=True)

    def __str__(self):
        return self.email
from django.db import models


class Gmail(models.Model):
    message = models.TextField()
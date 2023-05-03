from django.db import models
from django.db.models.signals import post_save
from ckeditor.fields import RichTextField
from django.conf import settings


class Tag(models.Model):
    title = models.CharField(max_length=221)

    def __str__(self):
        return self.title


class Blog(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length=221)
    description = RichTextField()
    image = models.ImageField(upload_to='blog_image/')
    tags = models.ManyToManyField(Tag)
    created_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title


class SubContent(models.Model):
    blog = models.ForeignKey(Blog, on_delete=models.CASCADE, related_name='subcontent')
    title = models.CharField(max_length=221)
    image = models.ImageField(upload_to='blog_image')
    description = RichTextField()


class Comment(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    blog = models.ForeignKey(Blog, on_delete=models.CASCADE, related_name='comments')
    message = models.TextField()
    parent_comment = models.ForeignKey('self', on_delete=models.CASCADE, null=True, blank=True)
    top_level_comment_id = models.IntegerField(null=True, blank=True)
    created_date = models.DateTimeField(auto_now_add=True)

    @property
    def get_related_comments(self):
        qs = Comment.objects.filter(top_level_comment_id=self.id).exclude(id=self.id)
        if qs:
            return qs
        else:
            return None


def comment_post_save(instance, sender, created, *args, **kwargs):
    if created:
        top_level_comment = instance
        while top_level_comment.parent_comment:
            top_level_comment = top_level_comment.parent_comment
        instance.top_level_comment_id = top_level_comment.id
        instance.save()


post_save.connect(comment_post_save, sender=Comment)
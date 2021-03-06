from django.db import models
from django.contrib.auth.models import User


class Post(models.Model):
    """ Blog Model """
    user = models.ForeignKey(
        User, related_name="posts", on_delete=models.CASCADE,
        null=True, blank=True)
    created = models.DateField(auto_now_add=True)
    updated = models.DateField(auto_now=True)
    title = models.CharField(max_length=255)
    post = models.TextField(max_length=500000)
    image_url = models.URLField(max_length=1024, null=True, blank=True)
    image = models.ImageField(null=True, blank=True)

    def __str__(self):
        return str(self.title)

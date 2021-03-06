from django.db import models
from django.contrib.auth.models import User


class Newsletter(models.Model):
    """ Newsletter Model """
    newsletter = models.ForeignKey(
        User, related_name="newsletter", on_delete=models.CASCADE,
        null=True, blank=True)
    email = models.CharField(max_length=255)
    email_confirmation = models.CharField(max_length=250)
    categories = models.ForeignKey(
        'products.Category', null=True, blank=True, on_delete=models.SET_NULL
    )

    def __str__(self):
        return self.name

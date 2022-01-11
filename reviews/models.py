from django.db import models
from django.contrib.auth.models import User
from products.models import Product


class Category(models.Model):

    class Meta:
        verbose_name_plural = 'Categories'
        
    name = models.CharField(max_length=254)
    friendly_name = models.CharField(max_length=254, null=True, blank=True)

    def __str__(self):
        return self.name

    def get_friendly_name(self):
        return self.friendly_name

class Review(models.Model):
    """ Review Model """
    user = models.ForeignKey(
        User, related_name="reviews", on_delete=models.CASCADE,
        null=True, blank=True)
    products = models.ForeignKey(
        Product, related_name="reviews", on_delete=models.CASCADE)
    created = models.DateField(auto_now_add=True)
    updated = models.DateField(auto_now=True)
    title = models.CharField(max_length=255)
    review = models.TextField(max_length=500)
    category = models.ForeignKey('Category', null=True, blank=True, on_delete=models.SET_NULL)

    def __str__(self):
        return str(self.title)

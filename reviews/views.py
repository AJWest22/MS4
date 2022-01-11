from django.shortcuts import render, reverse, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.db.models.functions import Lower

from .models import Review
from .forms import ReviewForm

""" Gets all reviews """
def reviews(request):
    reviews = Review.objects.all()
    sort = None
    direction = None

    template = 'reviews/reviews.html'

    context = {
        'reviews': reviews,
    }

    return render(request, template, context)

from django.shortcuts import render, reverse, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.db.models.functions import Lower
from .models import Product

from .models import Review
from .forms import ReviewForm


""" Gets all reviews """
def reviews(request):

    reviews = Review.objects.all()

    template = 'reviews/reviews.html'

    context = {
        'reviews': reviews,
    }

    return render(request, template, context)

@login_required
def add_review(request):
    """ Adds reviews """

    if not request.user.is_authenticated:
        messages.error(request, 'Sorry only registered users can do that.')
        return redirect(reverse('home'))

    if request.method == 'POST' and request.user.is_authenticated:
        form = ReviewForm(request.POST)
        if form.is_valid():
            review = form.save()
            review.user = request.user
            review.save()
            messages.success(request, "Your review has" +
                             "been submitted for this game")
        else:
            messages.error(request, 'Sorry, we couldn''t' +
                           'submit you review right now')

    template = 'reviews/add_review.html'
    context = {
        'form': form,
    }
    return render(request, template, context)

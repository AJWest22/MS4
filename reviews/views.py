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
            return redirect('reviews')
        else:
            messages.error(request, 'Sorry, we couldn''t' +
                           'submit you review right now')    
    else:
        form = ReviewForm()

    template = 'reviews/add_review.html'
    context = {
        'form': form,
    }
    return render(request, template, context)

@login_required
def edit_review(request, review_id):
    """ Edits a review of a product """
    if not request.user.is_authenticated:
        messages.error(request, 'Sorry, only the reviewer can edit a review.')
        return redirect(reverse('reviews'))

    review = get_object_or_404(Review, pk=review_id)
    if request.method == 'POST':
        form = ReviewForm(request.POST, instance=review)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your review has been updated!')
            return redirect(reverse('edit_review', args=[review.id]))
        else:
            messages.error(request, 'Your review failed to update. Please check the form is filled out correctly.')
    else:
        form = ReviewForm(instance=review)
        messages.info(request, f'You are editing {review.id}')

    template = 'reviews/edit_review.html'
    context = {
        'form': form,
        'review': review,
    }

    return render(request, template, context)

@login_required
def delete_review(request, review_id):
    """ Remove reviews of the products """

    review = get_object_or_404(Review, pk=review_id)
    if request.user.is_superuser or review.username == request.user:
        review.delete()
        messages.success(request, "Review has been successfully deleted"
                         )
    else:
        messages.error(request, 'Sorry, we could not' +
                       'delete you review right now')

    return redirect(reverse('reviews'))

from django.shortcuts import render, reverse, redirect, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required

from .models import Newsletter
from .forms import NewsletterForm


@login_required
def newsletter(request):
    """ Displays newsletter signup form. """
    if not request.user.is_authenticated:
        messages.error(request, 'Sorry only registered users can do that.')
        return redirect(reverse('home'))

    if request.method == 'POST' and request.user.is_authenticated:
        form = NewsletterForm(request.POST)
        if form.is_valid():
            newsletter = form.save()
            newsletter.save()
            messages.success(request, "You have successfully signed up to our monthly newsletter")
            return redirect('home')
        else:
            messages.error(request, 'Sorry, we couldn''t' +
                           'sign you up right now')
    else:
        form = NewsletterForm()

    template = 'newsletter/newsletter.html'
    context = {
        'form': form,
    }
    return render(request, template, context)

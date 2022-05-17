from django.shortcuts import render, reverse, redirect, get_object_or_404
from django.contrib import messages

from .models import Newsletter
from .forms import NewsletterForm


def newsletter(request):
    """ Displays newsletter signup form. """

    if request.method == 'POST':
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

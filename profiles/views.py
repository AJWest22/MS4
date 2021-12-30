from django.shortcuts import render

from .models import UserProfile


def profile(request):
    """ Displays a user's profile. """
    profile = get_object_or_404(UserProfile, user=request.user)

    template = 'profiles/profile.html'
    context = {}

    return render(request, template, context)


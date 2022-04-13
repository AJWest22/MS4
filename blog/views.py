from django.shortcuts import render, reverse, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.db.models.functions import Lower

from .models import Blog
from .forms import BlogForm


""" Gets all reviews """
def posts(request):

    posts = Blog.objects.all()

    template = 'blog/blog.html'

    context = {
        'posts': posts,
    }

    return render(request, template, context)


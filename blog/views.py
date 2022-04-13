from django.shortcuts import render, reverse, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.db.models.functions import Lower

from .models import Post
from .forms import PostForm


""" Gets all blog posts """
def posts(request):

    posts = Post.objects.all()

    context = {
        'posts': posts,
    }

    return render(request, 'blog/blog.html', context)


@login_required
def add_post(request):
    """ Adds blog posts """

    if not request.user.is_superuser:
        messages.error(request, 'Sorry only site admins can do that.')
        return redirect(reverse('home'))

    if request.method == 'POST' and request.user.is_superuser:
        form = ReviewForm(request.POST)
        if form.is_valid():
            post = form.save()
            post.user = request.user
            post.save()
            messages.success(request, "Your post has" +
                             "been submitted for this blog")
            return redirect('reviews')
        else:
            messages.error(request, 'Sorry, we couldn''t' +
                           'submit you post right now')    
    else:
        form = PostForm()

    template = 'blog/add_blog.html'
    context = {
        'form': form,
    }
    return render(request, template, context)
